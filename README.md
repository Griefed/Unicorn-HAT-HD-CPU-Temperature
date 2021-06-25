# Unicorn HAT HD CPU Temperature

[[_TOC_]]

Displays the CPU Temperature in fancy rainbow colours or in different colours depending on the CPU temperature. You choose!

Should the temperature exceed 55°C, the text will be coloured red to get your attention!

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
