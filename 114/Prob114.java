/**
 * 
 */

/**
 * @author Darkaz
 *
 */
public class Prob114 {

	/**
	 * @param args
	 */
	 /**
	   * Methode recursive de comptage de lignes
	   */
	  public long nbLignes(int n) {
		    long somme;
		    // condition d'arret : s'il reste moins de 3 cases, une seule possibilite
		    if (n<3) {
		      return 1;
		    }
		    // pour l'instant, une possibilite
		    somme = 1;
		    // on ajoute un bloc d'au moins 3 cases a la ligne
		    for (int i=3 ; i<=n ; i++) {
		      // apres le bloc, on ajoute des cases vides
		      for (int j=1 ; j<=n-i+1 ; j++) {
			int k = n - i - j;
			// si k<0 : une seule possibilite
			if(k<0) {
			  somme++;
			  continue;
			}
			// il reste k cases a remplir
			somme += nbLignes(k);
		      }
		    }
		    return somme;
		  }

		  /**
		   * Methode recursive de comptage de lignes
		   */
		  public long nbLignes2(int n, long table[]) {
		    long somme;
		    // condition d'arret : s'il reste moins de 3 cases, une seule possibilite
		    if (n<3) {
		      return 1;
		    }
		    // pour l'instant, une possibilite
		    somme = 1;
		    // on ajoute un bloc d'au moins 3 cases a la ligne
		    for (int i=3 ; i<=n ; i++) {
		      // apres le bloc, on ajoute des cases vides
		      for (int j=1 ; j<=n-i+1 ; j++) {
			int k = n - i - j;
			// si k<0 : une seule possibilite
			if(k<0) {
			  somme++;
			  continue;
			}
			// il reste k cases a remplir
			if (table[k]>0) {
			  // deja dans la table
			  somme += table[k];
			} else {
			  // pas dans la table... a calculer
			  somme += nbLignes2(k, table);
			}
		      }
		    }
		    // si necessaire, ajouter la valeur dans la table
		    if (n>=0 && table[n]==0) {
		      table[n] = somme;
		    }
		    return somme;
		  }

		  public static void main(String args[]) {
		    int nb = 0;
		    Prob114 appli = new Prob114();
		    long table[];
		    // verification du nombre de parametres
		    if(args.length>0) {
		      // conversion du parametre en entier
		      nb = Integer.parseInt(args[0]);
		      // si nb<=30 : trier le tableau et l'afficher
		    }
		    else  {
		      System.err.println("Syntaxe : java prog nbElem");
		      // sortir du prog
		      System.exit(0);
		    }

		    table = new long[nb+1];

		    for (int i=1 ; i<=nb ; i++) {
		      System.out.println(i+" : "+appli.nbLignes2(i, table));
		    }
		  }
		}

