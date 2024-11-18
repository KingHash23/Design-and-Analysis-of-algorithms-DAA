from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Task representation
class Task:
    def __init__(self, task_id, title, task_type, start_time, end_time, priority):
        self.task_id = task_id
        self.title = title
        self.task_type = task_type  # 'personal' or 'academic'
        self.start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M')
        self.end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M')
        self.priority = priority

    def __repr__(self):
        return (f"{self.title} ({self.task_type}): "
                f"{self.start_time.strftime('%Y-%m-%d %H:%M')} - {self.end_time.strftime('%Y-%m-%d %H:%M')}, "
                f"Priority: {self.priority}")

# Weighted Interval Scheduling
def weighted_interval_scheduling(tasks):
    tasks.sort(key=lambda x: x.end_time)  # Sort tasks by end_time
    n = len(tasks)
    dp = [0] * (n + 1)
    task_indexes = [-1] * n  # To store the last non-overlapping task index

    def find_last_non_overlap(index):
        low, high = 0, index - 1
        while low <= high:
            mid = (low + high) // 2
            if tasks[mid].end_time <= tasks[index].start_time:
                if tasks[mid + 1].end_time <= tasks[index].start_time:
                    low = mid + 1
                else:
                    return mid
            else:
                high = mid - 1
        return -1

    # Precompute last non-overlapping task indexes
    for i in range(n):
        task_indexes[i] = find_last_non_overlap(i)

    # Fill DP table
    for i in range(1, n + 1):
        include_task = tasks[i - 1].priority + dp[task_indexes[i - 1] + 1]
        exclude_task = dp[i - 1]
        dp[i] = max(include_task, exclude_task)

    return dp[-1]

# Binary Search for Tasks
def binary_search_tasks(tasks, key, value):
    tasks.sort(key=lambda x: getattr(x, key))  # Sort by key
    low, high = 0, len(tasks) - 1
    while low <= high:
        mid = (low + high) // 2
        if getattr(tasks[mid], key) == value:
            return tasks[mid]
        elif getattr(tasks[mid], key) < value:
            low = mid + 1
        else:
            high = mid - 1
    return None

# Busy Time Slot Analysis
def analyze_busy_slots(tasks, interval=1):
    task_density = [0] * 24  # Hourly slots
    for task in tasks:
        start_hour = task.start_time.hour
        end_hour = task.end_time.hour
        for i in range(start_hour, end_hour + 1):
            task_density[i] += 1
    return task_density

# Visualize Task Schedule with Gantt Chart
def plot_gantt_chart(tasks):
    fig, ax = plt.subplots(figsize=(10, 6))
    yticks = []
    labels = []
    for i, task in enumerate(tasks):
        yticks.append(i + 1)
        labels.append(task.title)
        ax.barh(i + 1, (task.end_time - task.start_time).seconds / 3600,
                left=task.start_time.hour,
                color='skyblue', edgecolor='black')

    ax.set_yticks(yticks)
    ax.set_yticklabels(labels)
    ax.set_xlabel('Time (Hours)')
    ax.set_ylabel('Tasks')
    ax.set_title('Task Schedule')
    plt.grid(True)
    plt.show()

# Sample Usage
if __name__ == "__main__":
    # Example tasks
    tasks = [
        Task(1, "Morning Run", "personal", "2024-11-15 06:00", "2024-11-15 07:00", 2),
        Task(2, "Study Algorithms", "academic", "2024-11-15 09:00", "2024-11-15 11:00", 5),
        Task(3, "Team Meeting", "academic", "2024-11-15 14:00", "2024-11-15 15:00", 3),
        Task(4, "Grocery Shopping", "personal", "2024-11-15 16:00", "2024-11-15 17:00", 1),
        Task(5, "Dinner with Family", "personal", "2024-11-15 19:00", "2024-11-15 21:00", 4)
    ]

    # Weighted Interval Scheduling
    max_weight = weighted_interval_scheduling(tasks)
    print(f"Maximum Priority Achievable: {max_weight}")

    # Search for a specific task
    search_result = binary_search_tasks(tasks, 'title', "Study Algorithms")
    print(f"Task Found: {search_result}")

    # Analyze Busy Slots
    task_density = analyze_busy_slots(tasks)
    print(f"Hourly Task Density: {task_density}")

    # Visualize with Gantt Chart
    plot_gantt_chart(tasks)
