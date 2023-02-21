


1. Open and administrative terminal (Right-click on terminal icon, hover over Windows Terminal choice, then right-click and select "Run as Administrator" ) Run the installer
```powershell
cd ~/Downloads
```

2. Run the following command to download the osgeo installer
```powershell
curl https://download.osgeo.org/osgeo4w/v2/osgeo4w-setup.exe -o osgeo4w-setup.exe
```

3. Run the following command to begin the installation process. This will take a few minutes.
```powershell
./osgeo4w-setup.exe -q -k -r -A -s https://download.osgeo.org/osgeo4w/v2/ -P proj
```

When the installation is complete you should see the following in the terminal window:
```powershell
Ending OSGeo4W install
```

4. Close this terminal window.


