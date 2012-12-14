/**
 * 
 */

/**
 * @author Matt
 * 
 */
public class Prob4 {

	/**
	 * @param args
	 */

	// test si nb est un palindrom
	public boolean palindrom(int nb) {
		boolean palindrom = false;
		if ((nb / 100000 == nb % 10 && (nb / 10000) % 10 == (nb / 10) % 10)
				&& (nb / 1000) % 10 == (nb % 1000) / 100)
			palindrom = true;
		return palindrom;
	}

	// effectue des produits et affiche le plus grand palindrom
	public void prod() {
		int prod = 0;
		int a = 0;
		int b = 0;
		for (int i = 100; i < 1000; i++)
			for (int j = 100; j < 1000; j++)
				if (palindrom(i * j) && (prod < i * j)) {
					prod = i * j;
					a = i;
					b = j;
				}

		System.out.println(prod + " = " + a + " * " + b);

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Prob4 ap = new Prob4();
		ap.prod();
	}

}
