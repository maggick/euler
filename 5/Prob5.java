/**
 * 
 */

/**
 * @author Darkaz
 * 
 */
public class Prob5 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		boolean b = false;
		int k = 1;
		// tant que le boolean est faux, cad qu'on a pas trouver un nombre on continue
		// optimisation ? mettre un pas ??
		while (!b) {
			k++;
			int c = 0;
			// il faut que k soit divisble pas tous les nb de 1 à 20
			// optimisation ? pas besoin de les tester tous (les premiers comme 2, 3, 7 ...)
			for (int i = 1; i <= 20; i++)
				if (k % i == 0)
					c++;
			if (c == 20)
				b = true;
		}
		System.out.println(k);

	}

}
