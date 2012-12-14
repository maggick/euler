/**
 * 
 */

/**
 * @author Darkaz
 *
 */
public class Prob6 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int somc = 0 ;
		int somm = 0 ;
		for (int i = 0; i<= 100 ; i++ ) {
			somc = somc + i*i;
			somm = somm + i;
		}
		int res = somm*somm - somc  ;
		System.out.println(res);
			

	}

}
