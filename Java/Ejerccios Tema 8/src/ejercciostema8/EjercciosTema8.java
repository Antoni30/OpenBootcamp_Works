
package ejercciostema8;


public class EjercciosTema8 {

   
    public static void main(String[] args) {
      Persona objPersona = new Persona();
      objPersona.setEdad(23);
      objPersona.setNombre("Antoni");
      objPersona.setTelefono("0987654321");
      System.out.println(objPersona.getNombre()+"\n"+objPersona.getEdad()+"\n"+objPersona.getTelefono());
    }

}
