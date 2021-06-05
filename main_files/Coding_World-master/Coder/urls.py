from django.urls import path, include
from . import views




urlpatterns=[    
         
    path('',views.Home),
    path('Signup/',views.Signup),
    path('login/',views.Login),
    path('home/',views.home),


    path('blog/',views.blog),
    path('python/',views.python),
    path('django/',views.djangos),
    path('cplus/',views.cplus),
    path('kotlin/',views.kotlin),
    path('java/',views.java),
    path('machine/',views.machine),
    path('sciense/',views.sciense),
    path('swift/',views.swift),
    path('css/',views.css),
    path('php/',views.php),
    path('js/',views.js),
    path('html/',views.html),
    path('c/',views.c),
    path('bootstrap/',views.boot),
    path('course/',views.course),
    path('r/',views.r),
    path('flask/',views.flask),
    path('contact/',views.Contact),
    path('editor/',views.editor),
    path('python_blog/',views.python_blog),
    path('python_basics/',views.tech),

    path('python_numpy/',views.numpy),
    path('python_pandas/',views.pandas),
    path('python_matplotlib/',views.matplot),
    path('python_tkinter/',views.tkinter),
    path('python_turtle/',views.turtle),
    path('python_pygame/',views.pygame),
    path('python_opencv/',views.opencv),
    path('python_kivy/',views.kivy),
    path('python_data_structure/',views.data_structure),
    path('python_database/',views.data_base),
    path('python_web_scrapping/',views.web_scrapping),
    path('python_django/',views.django_vidoes),
    path('python_flask/',views.flask_vidoes),
    path('python_data_sciense/',views.data_sciense),
    path('python_basics_modules/',views.basic_modules),  
    path('python_advanced_modules/',views.advanced_modules),





    path('c_sharph_programming/',views.c_sharph_vidoes),
    path('c_programming/',views.c_lang_vidoes),
    path('c++_programming/',views.c_plus_vidoes),
    path('java_programming/',views.java_vidoes),
    path('kotlin_programming/',views.kotlin_vidoes),
    path('swift_programming/',views.swift_vidoes),
    path('golang_programming/',views.golang_vidoes),
    path('r_programming/',views.r_pro_vidoes),
    path('html_programming/',views.html5_vidoes),
    path('css_programming/',views.css3_vidoes),
    path('bootstrap_programming/',views.bootstrap_vidoes),
    path('javascript_programming/',views.javascript_vidoes),
    path('php_programming/',views.php_vidoes),
    path('jquery_programming/',views.jquery_vidoes),
    path('java_app/',views.java_app_vidoes),
    path('flutter_app/',views.flutter_app_vidoes),
    path('docker/',views.docker_vidoes),
    path('Aws/',views.aws_vidoes),
    path('react_js/',views.react_js_vidoes),
    path('asp_net/',views.asp_net_vidoes),
    path('git_toturial/',views.github_vidoes),
    path('linux/',views.linux_vidoes),
    path('ruby_programming/',views.ruby_vidoes),
    

  #  path('login/',views.Contact),

]
    