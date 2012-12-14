/**
 * 
 */

/**
 * @author Darkaz
 * 
 */

// programme qui decompose un nombe en produit de ces facteur premieres
// marche correctement
// MARCHE, il fallait rajouter un L deriere le nombre !!
public class Prob3v2 {

	/**
	 * @param args
	 */

	public long traiter(long nb) {
		int i = 2;
		while (i < Math.sqrt(nb)) {
			if (nb % i != 0)
				i++;
			else {
				System.out.println(i);
				nb /= i;
			}
		}
		System.out.println(nb);
		return nb;
	}

	public boolean nbPremier(long n, long nb) {
		return n == nb;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Prob3v2 ap = new Prob3v2();
		long nb = 23586L;
		// int n = 0 ;
		ap.traiter(nb);
	}

}
