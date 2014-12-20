import sys

def init_from_args(obj, just_args=True):
  """ initialise self.* for all caller function local variable.
  if just_args=False, only caller function paramaters are used. """
  caller_name = sys._getframe(1).f_code.co_name
  code_obj = sys._getframe(1).f_code
  for key, value in sys._getframe(1).f_locals.items():
    if ((not just_args)
        or key in code_obj.co_varnames[1:code_obj.co_argcount]):
      setattr(obj, key, value)
