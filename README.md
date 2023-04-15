# gimp-plugin-hello-world
a mvp for creating a gimp plugin

Instructions
* Install gimp
* Install latest python3
* Install gimp dev tools

```bash
sudo apt-get install libgimp2.0-dev
```

verify with

```bash
pkg-config --cflags --libs gimpui-2.0
```

create a pluggin like the hello_world.py provided.

copy the pluggin to the gimp plugins directory

if you are using the WSL and have it installed on windows it might be here YMWV.
```
export winUser=$(powershell.exe '$env:UserName' | tr -dc '[:alnum:]')
ls "/mnt/c/Users/$winUser/AppData/Local/Programs/GIMP 2/lib/gimp/2.0/plug-ins/"
```


copy the plugin 
```bash
cp hello_world.py "/mnt/c/Users/$winUser/AppData/Local/Programs/GIMP 2/lib/gimp/2.0/plug-ins/"
```
