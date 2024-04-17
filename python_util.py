def get_loaded_libraries():
    import os
    import psutil
    p = psutil.Process(os.getpid())
    for lib in p.memory_maps():
      print(lib.path)
