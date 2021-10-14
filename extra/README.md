# CS61A Extras

### Multiprocessing

[Ray](https://github.com/ray-project/tutorial)

Usual imports and header
```python
import ray
import time
ray.init(num_cpus=4, ignore_reinit_error=True, include_webui=False) # starts processes
```

```@ray.remote``` decorator
```python

@ray.remote
def slow_function():
  return 1
# slow_function.remote() returns ObjectID
# ray.get(slow_function.remote()) evaluates

# These happen in parallel.
for _ in range(4):
   slow_function.remote()

results = ray.get([slow_function.remote(i) for i in range(4)])

```
