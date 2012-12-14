/**
 * 
 */

/**
 * @author Darkaz
 * 
 */
public class prob2 {

	// calcul de fibo au rang n
	public int fibo2(int n, int acc, int accb) {
		if (n == 0)
			return accb;
		else if (n == 1)
			return acc;
		else
			return fibo2(n - 1, acc + accb, acc);
	}

	// la suite de fibo depasse 4 million au rang 33
	public static void main(String[] args) {
		prob2 f = new prob2();
		int res = 0;
		// on calcul fibo du rang 0 a 33 et si c est pair on somme
		for (int k = 0; k <= 33; k++) {
			int n = f.fibo2(k, 1, 0);
			if (n>0 && n%2==0)
				res = res +n ;
			if (n<0 && n%2==0)
				res = res -n ;
				
		}
		System.out.println("somme = " + res);
	}

}