/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejercicios.tema3;

/**
 *
 * @author user
 */
public class EjerciciosTema3 {

    public static int suma(int a, int b,int c){
        return a+b+c;
    }
    public static void main(String[] args) {
       //Primera Parte
       int resultado = suma(5,6,7);
       System.out.println(resultado);
       //Segunda Parte
       Coche miCoche = new Coche();
       miCoche.aumentar();
        System.out.println("Numero de Puertas: "+miCoche.getNumPuertas());
    }
    
}
