# Unicorn HAT HD CPU Temperature

Displays the CPU Temperature in fancy rainbow colours

Should the temperature exceed 55°C, the text will be coloured red to get your attention!
  If you want to change the temperature at which the alarms go off, look for the variable "warning" and change it's value accordingly.

If you can't start the script, remember to :
```bash
sudo chmod +x cpu.py
```

If you want to run the script in a screen (in the background):
```bash
screen -d -m -S CPU ./cpu.py
```


Re-attach to the screen using:
```bash
screen -r CPU
```

If screen isn't installed on your system:
```bash
sudo apt-get install screen
```
