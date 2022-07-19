/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author user
 */
public class EjerciciosTema4 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int numeroIf=4,numeroWhile=0,estacion=4;
        //literal a
        if(numeroIf>0){
            System.out.println(numeroIf+" es postitivo");
        }
        else if(numeroIf==0){
            System.out.println(numeroIf+" es 0");
        }
        else{
            System.out.println(numeroIf+" es negativo");
        }
        //Literal b
        while(numeroWhile<3){
            numeroWhile++;
            System.out.println(numeroWhile);
        }
        //Literal c
        do{
            numeroWhile++;
            System.out.println(numeroWhile);
        }while(numeroWhile==3);
        //Literal d
        for (int numeroFor=0; numeroFor<=3;numeroFor++){
            System.out.println(numeroFor);
        }
        //Literal e
        switch(estacion){
            case 1:
                System.out.println("Primavera");
                break;
            case 2:
                System.out.println("Verano");
                break;
            case 3:
                System.out.println("Invierno");
                break;
            case 4:
                System.out.println("Otoño");
                break;
            default:
                System.out.println("NO existe esa esatcion");
        }
        
        
    }
    
}
