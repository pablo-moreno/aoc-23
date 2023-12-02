# What I learned

Didn't know that all the properties in the dataclass were mandatory at instantiation by default, but it actually makes sense.

```python
from day_02.utils import Game

game = Game()  # Does not raise exception
game.id        # Raises attribute exception
```
