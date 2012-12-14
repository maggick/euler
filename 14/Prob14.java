/**
 * 
 */

/**
 * @author Darkaz
 * 
 */

// une suite tend vers 1 pour tous les entiers positif
//on cherche quel nombre comprit entre 1 et 1 million
//demande le plus d'iteration afin d'etre a 1
public class Prob14 {

	/**
	 * @param args
	 */
	public long cont = 0;
	public long res = 0;
	public long nb = 0;

	// methode recursive de la suite => stackoveerflow
	public long suite(long n, long c) {
		if (n == 1)
			return 1;
		if (n % 2 == 0)
			n /= 2;
		else
			n = n * 3 + 1;
		// System.out.println(n);
		if (c > cont) {
			this.cont = c;
			this.res = this.nb;
		}
		return suite(n, c + 1);
	}

	// methode itterative de la suite
	public long suite2(long n) {
		long c = 0;
		while (n != 1) {
			if (n % 2 == 0)
				n /= 2;
			else
				n = n * 3 + 1;
			c++;
			//System.out.println(n);
		}
		return c;
	}

	// boucle entre 13 et 1 million
	public void boucle() {
		for (long i = 13; i < 1000000; i++) {
			long c = suite2(i);
			if (c > this.cont) {
				this.cont = c;
				this.nb = i;
			}
			System.out.println(i);
		}
		System.out.println(nb);
	}

	//le main, lance la boucle
	public static void main(String[] arg) {
		Prob14 ap = new Prob14();
		ap.boucle();
	}
}
