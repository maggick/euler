/**
 * 
 */

/**
 * @author Matt
 * 
 */
public class Prob11 {

	/**
	 * @param args
	 */
	// marche correctement
	// program dans lequel on entre une chaine de caractere du type 02 56 76 15
	// 28 19 68
	// on va chercher quel est le plus grand produit de 4 entier (en ligne
	// colone
	public int[][] saisie(String[] args) {
		int n = 0;
		int tab[][] = new int[20][20];
		for (int i = 0; i < 20; i++)
			for (int j = 0; j < 20; j++) {
				tab[i][j] = Integer.parseInt(args[n]);
				n++;
			}
		return tab;
	}

	// effectue le produit sur les lignes
	public int prodLigne(int[][] tab) {
		int res = 0;
		for (int i = 0; i < tab.length; i++)
			for (int j = 0; j < tab[0].length - 3; j++) {
				int prod = tab[i][j] * tab[i][j + 1] * tab[i][j + 2]
						* tab[i][j + 3];
				if (prod > res)
					res = prod;
			}
		return res;
	}

	// effectue le produit sur les colonnes
	public int prodColonne(int[][] tab) {
		int res = 0;
		for (int i = 0; i < tab.length - 3; i++)
			for (int j = 0; j < tab[0].length; j++) {
				int prod = tab[i][j] * tab[i + 1][j] * tab[i + 2][j]
						* tab[i + 3][j];
				if (prod > res)
					res = prod;
			}
		return res;
	}

	// effectue le produit sur la diagonal montante
	public int prodDiagoMont(int[][] tab) {
		int res = 0;
		for (int i = 3; i < tab.length; i++)
			for (int j = 0; j < tab[0].length - 3; j++) {
				int prod = tab[i][j] * tab[i - 1][j + 1] * tab[i - 2][j + 2]
						* tab[i - 3][j + 3];
				if (prod > res)
					res = prod;
			}
		return res;
	}

	// effectue le produit sur la diagonal descendante
	public int prodDiagoDes(int[][] tab) {
		int res = 0;
		for (int i = 0; i < tab.length - 3; i++)
			for (int j = 0; j < tab[0].length - 3; j++) {
				int prod = tab[i][j] * tab[i + 1][j + 1] * tab[i + 2][j + 2]
						* tab[i + 3][j + 3];
				if (prod > res)
					res = prod;
			}
		return res;
	}

	// affiche la grille
	public void affichage(int[][] tab) {
		for (int i = 0; i < tab.length; i++) {
			for (int j = 0; j < tab[0].length; j++)
				System.out.print(tab[i][j] + " ");
			System.out.println();
		}
	}

	// teste le max
	public int max(int a, int b, int c, int d) {
		int max = 0;
		if (a > max)
			max = a;
		if (b > max)
			max = b;
		if (c > max)
			max = c;
		if (d > max)
			max = d;
		return max;
	}

	// le main
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Prob11 ap = new Prob11();
		int tab[][] = new int[0][0];
		tab = ap.saisie(args);
		// ap.affichage(tab);
		int a = ap.prodColonne(tab);
		int b = ap.prodDiagoMont(tab);
		int c = ap.prodLigne(tab);
		int d = ap.prodDiagoDes(tab);
		int prod = ap.max(a, b, c, d);
		// System.out.println(a+" "+b+" "+c +" "+d);
		System.out.println(prod);
	}
}
