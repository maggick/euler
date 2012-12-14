/**
 * 
 */

/**
 * @author Darkaz
 * 
 */
public class Prob3 {
	// programme qui decompose un nombe en produit de ces facteur premieres
	// decompose un nombre en produit de ces facteurs premier
	// NE MARCHE pas pour un grand nombre (stack overflow), il faut utiliser un prog iteratif
	public int decompo(int n, long nb) {
		if (n == nb) {
			System.out.println(n);
			return n;
		} else if (nb % n == 0) {
			System.out.println(n);
			return decompo(n, nb / n);
		} else
			return decompo(n + 1, nb);
	}

	public static void main(String[] args) {
		Prob3 meth = new Prob3();
		long nb = 220 ;
		meth.decompo(2, nb);
	}
}