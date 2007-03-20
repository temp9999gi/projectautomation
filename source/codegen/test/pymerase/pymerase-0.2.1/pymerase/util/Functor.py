class Functor:
  def __init__(self, function, *args, **kargs):
    assert callable(function), "function should be a callable obj"
    self._function = function
    self._args = args
    self._kargs = kargs
    
  def __call__(self, *args, **kargs):
    """call function"""
    _args = list(self._args)
    _args.extend(args)
    _kargs = self._kargs.copy()
    _kargs.update(kargs)
    return apply(self._function,_args,_kargs)      

