# What is a gradient 
A gradient is a matrix of partial derivates, one with respect to each indendant variable of the scalar function *`f`*, which gives the direction of steepest **ascent**.

Then the gradient is found using the general equation: 

<div>
  <img style="vertical-align:middle" src="https://latex.codecogs.com/svg.image?\small&space;\nabla&space;f(x_{0},x_{1},\ldots,x_{n})=\begin{bmatrix}&space;\frac{\partial&space;f}{\partial&space;x_{0}}&space;\\&space;\frac{\partial&space;f}{\partial&space;x_{1}}&space;\\&space;\vdots&space;\\&space;\frac{\partial&space;f}{\partial&space;x_{n}}\end{bmatrix}&space;">
 <span style='margin-right:1.25em; display:inline-block;'>&emsp; (Equation 1)</span>
</div>

<br />


## Example:

If a function is:
<div>
  <img style="vertical-align:middle" src="https://latex.codecogs.com/svg.image?\small&space;f(x_{0},x_{1},x_{2})&space;=&space;x_{0}^{2}x_{1}^{3}x_{2}&space;&plus;&space;x_{2}^{2}&space;">
 <span style='margin-right:1.25em; display:inline-block;'>&emsp; (Equation 2)</span>
</div>

<br />

The resulting gradient of the function is: 

<div>
  <img style="vertical-align:middle" src="https://latex.codecogs.com/svg.image?\small&space;\nabla&space;f(x_{0},x_{1},x_{2})&space;=&space;(2x_{0}x_{1}^3x_{2},&space;3x_{0}^2x_{1}^2x_{2},&space;x_{0}^2x_{1}^3&plus;2x_{2})">
 <span style='margin-right:1.25em; display:inline-block;'>&emsp; (Equation 3)</span>
</div>

* Note: Will be following both the syntax displayed here and the syntax used as Equation 1 interchangably. They are both a vector of derivative functions.

<br />

# Greatest Rate of Change - Steepest Descent
Purpose:

Intuition: 
- What direction will a marble roll on the surface of a plane, given it falls on given point.
- How far will it roll on the plane.

Theory: 
- Given a function *`f`* for a surface, find the maximum rate of change. Which is done by:
   1. Finding the gradient for that function.
   2. Given a point, find the `Resultant Vector` at the point.
- `Resultant Vector` will have both a direction and magnitude.

<p align="center">
<img src="imgs\Gradient_Kandasamy_Illanko.png" alt="drawing" width="450", class="center"/>
    <br>
    <em>Fig.1 - Surface of plane.</em>
    
</figure>
</p>

## Example:

```
Find the direction and magnitude of the greatest rate of change of equation 2 at point (1,2,3).
```

Solution: 
1. Gind the gradient for the function. (Already done - Equation 3)
<div>
  <img style="margin-left:3.25em" src="https://latex.codecogs.com/svg.image?\small&space;\nabla&space;f(1,2,3)&space;=&space;(2(1)(2)^3(3),&space;3(1)^2(2)^2(3),&space;(1)^2(2)^3&plus;2(3))" >
  
2. Calculate Vector:

  <img style="margin-left:3.25em" src="https://latex.codecogs.com/svg.image?\small&space;\nabla&space;f(1,2,3)&space;=&space;(48,36,14)" >
  
  <img style="margin-left:3.25em" src="https://latex.codecogs.com/svg.image?\small&space;\nabla&space;f(1,2,3)&space;=&space;(24,18,7)" >

3. Calculate magnitude:

  <img style="margin-left:3.25em" src="https://latex.codecogs.com/svg.image?\small&space;&space;\left\|&space;\nabla&space;f(1,2,3)&space;\right\|&space;=&space;\sqrt{48^2&plus;36^2&plus;14^2}" >

  <img style="margin-left:3.25em" src="https://latex.codecogs.com/svg.image?\small&space;&space;\left\|&space;\nabla&space;f(1,2,3)&space;\right\|&space;\approx&space;&space;61.61" >
</div>

Key points:
- The direction of the steepest descent is negative of the gradient. 
- If you want to know the path of a ball will travel on the surface, you must calculate the gradient at `n` intervals. 
    - To accompish going in steps, take the direction and multiply by it `N` such that `N < 1`. **`N`** is the **`Step Size`**.
- The `Step Size` is what determines how far to travel in a direction. 

```
Does the magnitude of the gradient effect my displacement, given that I keep my step size the same?
```

## Rate of change on a given vector

Simply find the project of the resultant gradient on the unit vector of the vector in question. 

Use the following 


# Quick Maths

