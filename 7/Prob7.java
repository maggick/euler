/**
 * @author Darkaz
 * 
 */

// trouve le ième nombre premier
public class Prob7 {

	/**
	 * @param args
	 */

	// le dernier nombre afficher dans la console est le ième nombre premier
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Prob3v2 fct = new Prob3v2();
		int n = 3;
		int c = 0;
		while (c <= 10001 - 2) { //on rentre ici le ième nombre premier que l'on souhaite 
			if (fct.nbPremier(fct.traiter(n), n))
				c++;
			n+=2;
		}
		System.out.println(n-2);
	}
}

// le 10001 eme nombre premier est 104743 (le prog marche mais l'affichage prend du temps)
