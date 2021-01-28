import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"
timeout = 30

# Logging details
print("Binding on : ", bind)
print("Spawned :", workers, " workers")
print("Using ", worker_class, " worker class")