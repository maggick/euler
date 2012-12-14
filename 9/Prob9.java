/**
 * 
 */

/**
 * @author Darkaz
 * 
 */
public class Prob9 {

	/**
	 * @param args
	 */

	// trouve a,b,b tel que a²+b² = c² et a+b+c=1000
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for (int i = 1; i <= 1000; i++)
			for (int j = 1; j <= 1000; j++) {
				int c = 1000 - i - j;
				if (c * c == i * i + j * j)
					System.out.println(i + " " + j + " " + c + " " + i * j * c);
			}
	}
}