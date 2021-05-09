# plymouth-themes

----
Plymouth
=
Plymouth is graphical boot animation and logger.

This only works on linux. You can use this themes in your linux pc. To use these follow the instructions below. 

-----
How to Use:
=

Follow these steps to install and run the sctipt.

```
git clone https://github.com/kingness-zero/plymouth-themes.git

cd plymouth-themes

# To install themes in your pc for the first time or to Update themes.
python3 kz_plymouth.py install

# To run The Sctipt
python3 kz_plymouth.py
```

From there You can choose a Theme or you can preview the Splash screen.

**Note**:You can only preview the chosen(Installed) theme. So install the Theme and Preview the theme.

-----
How to Install Without Using kz_plymouth.py Python Script:
=

```
git clone https://github.com/kingness-zero/plymouth-themes.git

cd plymouth-themes

sudo cp -r themes/* /usr/share/plymouth/themes/
```

Choose a theme.
you can use what ever theme you want from the list below.

sudo plymouth-set-default-theme -R (theme)

-------
Themes Available:
=
* batman

* birthdayocto

* godofwar

* harleyquinn

* daredevil

* lighter

* lonely

* loading

* covid19

* ironman

* r

```
sudo plymouth-set-default-theme -R daredevil
```
