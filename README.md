# Floroid
An (somewhat) python-ish language mainly for golfing purposes.

Import the Florolang module to run Floroid-code. Florolang module imports the 'functions' module, so that has to accessible as well.

    import Florolang;
    interpreter = Florolang.Floroid("z(fg([1,2,3]))")
    exec(interpreter.parse())

Output: 3
