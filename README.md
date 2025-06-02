# Práctica 2: Filtro de Kalman en ROS 2

Esta práctica ha sido realizada en el entorno de Gazebo con Ros2, tras la imposibilidad de poder ejecutar los códigos de tal forma que se puedan observar gráficas y resultados, se envía un código probado, que en principio debería funcionar de forma correcta pero sin la posibilidad de ejecutar los códigos y comprobarlo exahustivamente.

El filtro de Kalman se implementa para estimar la posicion y orientación de un robot en 2 casos diferentes.

"Filtro de kalman básico" donde solo se usa una matriz de transición A y una matriz de control B y "Filtro de kalman extendido" que añade además términos para la velocidad tanto linear como angular. Ambos tienen una matriz C de en el apartado de observación. 

Debido a lo explicado anteriormente no tengo ningún resultado que muestre como funcionaría la variación de los parámetros de error en el propio código. Lo que si puedo tener en cuenta es el funcionamiento del mismo, ya que si hubiese aumentado el error en el modelo de predicción, el filtro confiatía más en las propias mediciones. Y cuando el error alto se encuentra en las propias mediciones, el filtro confía más en su modelo de predicción.

Desafortunadamente, esto es lo que puedo tratar con los medios proporcionados en esta práctica.


