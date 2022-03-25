## Reto TC1001

You can use the [editor on GitHub](https://github.com/horny-pug/TC1001-Computer-Vision/edit/main/docs/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

## Integrantes

`Juan Pablo Ortiz Ortega`
`a01366969@tec.mx`

`Miguel Ángel Santamaria Vilchis`
`a01366795@tec.mx`

`Josué Jemuel Flores Nestor`
`a01367182@tec.mx`

`Jorge Alberto Flores Ponce`
`a01769059@tec.mx`



## Tabla de Contenidos

1. [Introducción](#Introduccion)
2. [Intención](#Intencion)
3. [Motivaciones del Curso](#Motivaciones)
4. [Definciones](#Definiciones)
   - [Kernel](#Kernel)
   - [Convolution](#Convolution)
6. [Uso de Kernels](#Uso-de-Kernels)
   - [Mexican Hat](#Mexican-Hat)
   - [Gaussian Blur](#Gaussian-Blur)


### Introduccion

Las personas tienden a tener una perspectiva lineal de la historia, sin embargo el crecimiento exponencial de la tecnología ha sido evidente en las décadas pasadas. En un abrir y cerrar de ojos hemos ido de computadores reservados para los militares a niños con dispositivos relativamente poderosos en sus bolsillos. 

Uno de los campos mayor crecimiento en la ingeniería de software es la _Inteligencia Artificial_ con técnicas como el _Image Processing_. Las técnicas usadas han ido madurando y se han vuelto lo suficientemente capaces para desempeñar actividades que van desde la [autentificación de rostros](https://www.cnet.com/news/politics/in-china-facial-recognition-public-shaming-and-control-go-hand-in-hand/) hasta la [detección de tumores malignos en pacientes](https://www.nature.com/articles/d41586-020-03157-9), aún nos queda mucho por recorrer pero es impresionante el avance logrado.

![Hi](https://miro.medium.com/max/503/1*hqbYnsyjfRcceQqrR_HOyA.jpeg)

> Imagen 1. Uso de la IA e Image Processing para la detección de rostros.


### Motivaciones del curso
Dentro de este curso de Semana Tec *TC1001: Herramientas computacionales: el arte de la programación* se busca acercar a los estudiantes a este tipo de tecnologías de _Image Processing_ y por medio de unos cuantos ejercicios hacer uso de las bibliotecas ya presentes en lenguajes de script como Python, a continuación demostraremos el uso de ciertos filtros o kernels dentro de una misma imagen y cual es el resultado.

### Definiciones

#### Kernel 
Un *kernel de imagenes* es una pequeña matrix usada para aplicar efectos a cierto mapa de bits. Este tipo de efectos o filtros que logramos por medio de aplicaciones como Photoshop, Gimp e incluso Instagram tienen por debajo un *kernel* que acentúa ciertas características o le brinda ciertos atributos a la imagen de entrada.

![imagen-kereenel](https://muthu.co/wp-content/uploads/2019/08/gaussian.png)
> Imagen 2. Uso de un kernel de blur.

#### Convolution
La convolución es una operación matemática simple que es fundamental para muchas operaciones del _Image Processing_. La convolución proporciona una forma de 'multiplicar' dos matrices de números, generalmente de diferentes tamaños, pero de la misma dimensión, para producir una tercera matriz de números de la misma dimensión.


![imagen-kernel](https://miro.medium.com/max/1010/1*jIv2CLxdXsxvx60Urc11Tw.png)
> Imagen 3. Representación de una convolución de matrices al aplicar un kernel.

### Kernels
#### Mexican Hat
El sombrero mexicano, o filtro Gaussiano-Laplace invertido, es un filtro. Suaviza los datos y elimina estructuras constantes o que varían lentamente (por ejemplo, el fondo). Es útil para la detección de picos o multiescala.

Este núcleo se deriva de una función gaussiana normalizada, calculando la segunda derivada.

#### Gaussian Blur

El desenfoque gaussiano es un tipo de desenfoque que utiliza la función gaussiana para calcular la transformación que se le aplica a cada pixel de la imagen

![equation](https://3.bp.blogspot.com/-cVNi7VZLB_A/V3WTNVSHSqI/AAAAAAAAAuY/J1SN00PpFGoYWgKLKo-Pa_UozqZXmDb4ACLcB/s1600/GaussianKernel.png)





