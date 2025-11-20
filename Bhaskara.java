import java.util.Scanner;

public class Bhaskara{
  public static double[] Calculo (float a, float b, float c){
    float delta = b * b - 4 * a * c;
    double[] resultado = new double[2];
    
    if (delta >= 0) {
      double raiz_delta = Math.sqrt(delta);
      
      double x_1_linha = ((b * -1) + raiz_delta) / (2 * a);
      double x_2_linha = ((b * -1) - raiz_delta) / (2 * a);
      
      resultado[0] = x_1_linha;
      resultado[1] = x_2_linha;
      
    } else {
      resultado[0] = Double.NaN;
      resultado[1] = delta;
    }
    
    return resultado;
  };
  
  public static void main (String [] args){

    float val_a, val_b, val_c;
    
    try(Scanner td = new Scanner(System.in)){
      
      System.out.print("Digite valor de A: ");
      val_a = stdin.nextFloat();
      
      System.out.print("Digite valor de B: ");
      val_b = stdin.nextFloat();
      
      System.out.print("Digite valor de C: ");
      val_c = stdin.nextFloat();
    
      
      // Para teste (1, 5, 6)
      double[] resultado = Calculo(val_a, val_b, val_c);
      
      if (Double.isNaN(resultado[0])) {
        System.out.println("Não trabalho com raízes imaginarias");
        System.out.printf("Seu delta deu %.2f", resultado[1]);
      } else {
        System.out.printf("X'  = %.2f\nX'' = %.2f", resultado[0], resultado[1]);
      }
    }cacth(Exception e){
      System.out.println("Erro");
    }    
  }    
}
