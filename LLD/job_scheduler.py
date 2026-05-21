"""
User should be able to schedule jobs
Jobs will have Task and Schedule
Task is work will need to be executed based on shedule
Schedule is cron, calender or once 
Job shoulbe stored for future execution
Scheduler should handle failed job execution 
Handle exception like unsuported job/task/schedule type

+++
Entities
JobScheduler(Facade or Orchestrator)
Job
Task
Schedule
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
import logging

# Set up logging for error handling tracking
logger = logging.getLogger("JobScheduler")


# ==========================================
# 1. EXCEPTIONS (Robust Error Handling)
# ==========================================
class SchedulerException(Exception):
    """Base exception for all scheduler errors."""
    pass

class UnsupportedTypeException(SchedulerException):
    """Raised when an unsupported job, task, or schedule type is encountered."""
    pass

class JobExecutionException(SchedulerException):
    """Raised when a task execution fails."""
    pass


# ==========================================
# 2. STRATEGY PATTERN: Tasks (Interface Segregation / Open-Closed)
# ==========================================
class Task(ABC):
    @abstractmethod
    def execute(self, params: dict) -> None:
        """Executes the specific piece of work."""
        pass


class EmailTask(Task):
    def execute(self, params: dict) -> None:
        to_email = params.get("to")
        subject = params.get("subject")
        if not to_email or not subject:
            raise JobExecutionException("Missing required email parameters.")
        print(f"Sending email to {to_email} with subject: '{subject}'")


class TextTask(Task):
    def execute(self, params: dict) -> None:
        phone = params.get("phone")
        message = params.get("message")
        if not phone or not message:
            raise JobExecutionException("Missing required text parameters.")
        print(f"Sending SMS to {phone}: {message}")


# ==========================================
# 3. STRATEGY PATTERN: Schedules (Open-Closed Principle)
# ==========================================
class Schedule(ABC):
    @abstractmethod
    def should_execute(self, current_time: datetime) -> bool:
        """Determines if the job is due for execution."""
        pass

    @abstractmethod
    def calculate_next_execution(self, current_time: datetime) -> Optional[datetime]:
        """Calculates the next runtime. Returns None if it shouldn't run again (e.g., 'ONCE')."""
        pass


class CronSchedule(Schedule):
    def __init__(self, cron_expression: str, next_run: datetime):
        self.cron_expression = cron_expression
        self._next_run = next_run

    def should_execute(self, current_time: datetime) -> bool:
        return current_time >= self._next_run

    def calculate_next_execution(self, current_time: datetime) -> Optional[datetime]:
        # In a real app, use a library like `croniter` to compute the actual next match
        print(f"Calculating next execution for Cron: {self.cron_expression}")
        return datetime.utcnow()  # Mocking next interval runtime


class CalendarSchedule(Schedule):
    def __init__(self, target_time: datetime):
        self.target_time = target_time
        self._has_run = False

    def should_execute(self, current_time: datetime) -> bool:
        return not self._has_run and current_time >= self.target_time

    def calculate_next_execution(self, current_time: datetime) -> Optional[datetime]:
        self._has_run = True
        return None  # Calendar events in this design run once at a specific date


class OnceSchedule(Schedule):
    def __init__(self, execution_time: datetime):
        self.execution_time = execution_time
        self._has_run = False

    def should_execute(self, current_time: datetime) -> bool:
        return not self._has_run and current_time >= self.execution_time

    def calculate_next_execution(self, current_time: datetime) -> Optional[datetime]:
        self._has_run = True
        return None


# ==========================================
# 4. CORE ENTITY: Job
# ==========================================
class Job:
    def __init__(self, job_id: str, task: Task, schedule: Schedule, params: dict):
        if not isinstance(task, Task):
            raise UnsupportedTypeException(f"Unsupported task type: {type(task)}")
        if not isinstance(schedule, Schedule):
            raise UnsupportedTypeException(f"Unsupported schedule type: {type(schedule)}")
            
        self.job_id = job_id
        self.task = task
        self.schedule = schedule
        self.params = params
        self.next_execution_time: Optional[datetime] = datetime.utcnow() # Initial seed

    def execute(self) -> None:
        try:
            self.task.execute(self.params)
        except Exception as e:
            raise JobExecutionException(f"Job {self.job_id} failed during task execution.") from e

    def update_schedule(self, current_time: datetime) -> None:
        self.next_execution_time = self.schedule.calculate_next_execution(current_time)


# ==========================================
# 5. REPOSITORY PATTERN: Storage (Dependency Inversion Principle)
# ==========================================
class JobRepository(ABC):
    @abstractmethod
    def save(self, job: Job) -> None: pass

    @abstractmethod
    def delete(self, job_id: str) -> None: pass

    @abstractmethod
    def get_due_jobs(self, current_time: datetime) -> List[Job]: pass


class InMemoryJobRepository(JobRepository):
    """Handles storage responsibility separately from scheduling execution rules."""
    def __init__(self):
        self._jobs: Dict[str, Job] = {}

    def save(self, job: Job) -> None:
        self._jobs[job.job_id] = job

    def delete(self, job_id: str) -> None:
        if job_id in self._jobs:
            del self._jobs[job_id]

    def get_due_jobs(self, current_time: datetime) -> List[Job]:
        return [
            job for job in self._jobs.values() 
            if job.next_execution_time and job.schedule.should_execute(current_time)
        ]


# ==========================================
# 6. ORCHESTRATOR / FACADE: JobScheduler
# ==========================================
class JobScheduler:
    def __init__(self, repository: JobRepository):
        # Dependency Inversion: We depend on the repository abstraction, not a concrete implementation
        self._repository = repository

    def schedule_job(self, job: Job) -> None:
        self._repository.save(job)
        print(f"Job {job.job_id} scheduled successfully.")

    def execute_due_jobs(self) -> None:
        current_time = datetime.utcnow()
        due_jobs = self._repository.get_due_jobs(current_time)

        for job in due_jobs:
            try:
                print(f"\n--- Executing Job: {job.job_id} ---")
                job.execute()
                
                # If successful, calculate the next runtime
                job.update_schedule(current_time)
                if job.next_execution_time:
                    self._repository.save(job)
                else:
                    self._repository.delete(job.job_id) # Clean up finished one-off jobs
                    
            except JobExecutionException as e:
                self.handle_failed_job(job, e)

    def handle_failed_job(self, job: Job, error: Exception) -> None:
        """Requirement: Scheduler should handle failed job execution."""
        logger.error(f"Execution failed for Job {job.job_id}. Error: {str(error)}")
        print(f"[ALERT] Recovery System: Job {job.job_id} failed! Retrying or logging metrics...")
        
        # Example strategy: simple progressive backoff or clean up
        # For this illustration, we will push the schedule forward so it doesn't loop forever
        job.update_schedule(datetime.utcnow())
        if job.next_execution_time:
            self._repository.save(job)
