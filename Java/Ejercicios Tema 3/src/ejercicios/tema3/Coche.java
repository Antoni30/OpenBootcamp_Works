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
public class Coche {
    
    private int numPuertas;

    public Coche() {
        this.numPuertas=0;
    }
    public void aumentar(){
        this.numPuertas++;
    }

    public int getNumPuertas() {
        return numPuertas;
    }
    
    
}
