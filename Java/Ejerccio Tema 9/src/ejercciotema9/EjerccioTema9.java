/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejercciotema9;

/**
 *
 * @author user
 */
public class EjerccioTema9 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       Cliente objCliente = new Cliente();
       objCliente.setEdad(23);
       objCliente.setNombre("Antoni");
       objCliente.setTelefono("0987654321");
       objCliente.setCredito(2.5);
        System.out.println(objCliente.getNombre()+"\n"+objCliente.getTelefono()+"\n"+objCliente.getEdad()+"\n"+objCliente.getCredito());
    }
    
}
