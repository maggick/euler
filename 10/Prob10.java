/**
 * 
 */

/**
 * @author Darkaz
 * 
 */
public class Prob10 {

	/**
	 * @param args
	 */
	
	// calcul la somme de tous les nombres premiers inferieur a n 
	// tres lent pour n grand (1h20 pour n = 2 million)
	public static void main(String[] args) {
	

		Prob3v2 fct = new Prob3v2();
		long n = 2;
		long som = 0;
		while (n <= 2000000) {
			if (fct.nbPremier(fct.traiter(n), n))
				som += n;
			n++;
		}
		System.out.println(som);

	}
}
//la somme de tous les nombres premieres inferieur à 2 million est 142913828922

