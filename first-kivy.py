Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import kivy
[INFO   ] [Logger      ] Record log in C:\Users\Mukul\.kivy\logs\kivy_19-10-21_43.txt
[INFO   ] [deps        ] Successfully imported "kivy_deps.gstreamer_dev" 0.1.17
[INFO   ] [deps        ] Successfully imported "kivy_deps.gstreamer" 0.1.17
[INFO   ] [deps        ] Successfully imported "kivy_deps.angle" 0.1.9
[INFO   ] [deps        ] Successfully imported "kivy_deps.glew" 0.1.12
[INFO   ] [deps        ] Successfully imported "kivy_deps.glew_dev" 0.1.12
[INFO   ] [deps        ] Successfully imported "kivy_deps.sdl2" 0.1.22
[INFO   ] [deps        ] Successfully imported "kivy_deps.sdl2_dev" 0.1.22
[INFO   ] [Kivy        ] v1.11.1
[INFO   ] [Kivy        ] Installed at "C:\Users\Mukul\AppData\Local\Programs\Python\Python37\lib\site-packages\kivy\__init__.py"
[INFO   ] [Python      ] v3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)]
[INFO   ] [Python      ] Interpreter at "C:\Users\Mukul\AppData\Local\Programs\Python\Python37\pythonw.exe"
>>> from kivy.app import App
[INFO   ] [Factory     ] 184 symbols loaded
[INFO   ] [Image       ] Providers: img_tex, img_dds, img_sdl2, img_gif (img_pil, img_ffpyplayer ignored)
>>> from kivy.uix.button import Label
[INFO   ] [Text        ] Provider: sdl2
>>> class HelloApp(App):
	def build(self):
		return Label(text='HELLO HOGWARTS!')

>>> if __name__=='__main__':
	HelloApp().run()

[INFO   ] [Window      ] Provider: sdl2
[INFO   ] [GL          ] Using the "OpenGL" graphics system
[INFO   ] [GL          ] GLEW initialization succeeded
[INFO   ] [GL          ] Backend used <glew>
[INFO   ] [GL          ] OpenGL version <b'3.3.0'>
[INFO   ] [GL          ] OpenGL vendor <b'NVIDIA Corporation'>
[INFO   ] [GL          ] OpenGL renderer <b'GeForce 210/PCIe/SSE2'>
[INFO   ] [GL          ] OpenGL parsed version: 3, 3
[INFO   ] [GL          ] Shading version <b'3.30 NVIDIA via Cg compiler'>
[INFO   ] [GL          ] Texture max size <8192>
[INFO   ] [GL          ] Texture max units <32>
[INFO   ] [Window      ] auto add sdl2 input provider
[INFO   ] [Window      ] virtual keyboard not allowed, single mode, not docked
[INFO   ] [Base        ] Start application main loop
[INFO   ] [GL          ] NPOT texture support is available


