〰Prezentarea aplicatiei〰

  Aceasta aplicatie are ca scop antrenarea unei inteligente artificiale, ce va trebui sa preia cerintele clientilor, urmand ca mai apoi sa o analizeze si sa genereze o oferta detaliata, ce va cuprinde:
  - descrierea aplicatiei solicitate
  - tehnologiile folosite
  - task-uri concrete si detaliate ce tin strict de cerintele clientului (ex: daca se doreste crearea unei aplicatii de gestionare a clientilor unei sali de fitness, se vor avea in vedere cerinte unice, cum ar fi o baza de date a clientilor, preturile abonamentelor de fitness, etc.)


〰Dependinte necesare / Concepte utilizate〰

  - Pentru inceput, s-a folosit platforma de testare AI numita Groq Playground (https://console.groq.com/playground), pentru a putea oferi AI-ului, scriptul necesar. LLM-ul folosit si antrenat a fost Llama3 (llama3-70b-8192). Dupa rularea scriptului, platforma iti pune la dispozitie posibilitatea de a vizualiza codul, folosind butonul "View Code".
  - Urmatorul pas este de a merge la sectiunea de API Keys (https://console.groq.com/keys) si de a genera o cheie de tip API pe care o vom folosi ulterior.
  - Mediul de programare utilizat a fost Visual Studio Code.
  - Odata ce codul a fost importat in VSC, se va deschide un terminal unde se va introduce si rula comanda: pip install groq

![1](https://github.com/andreiserban1/ClientApp/assets/127241869/a4dcb0cf-3469-41d3-8904-2696728af6d1)

  - Mai departe, in acelasi terminal, se va introduce si rula comanda: "$env:GROQ_API_KEY="{aici se va introduce API Key-ul generat cu Groq}"

![2](https://github.com/andreiserban1/ClientApp/assets/127241869/b1255708-8ed8-4980-af89-4721b650ca34)

〰Utilizarea propriu-zisa a aplicatiei〰

  - Dupa ce toti pasii de mai sus au fost efectuati, se va rula codul, iar clientul va trebui sa introduca de la tastatura cerinta sa, iar AI-ul va incepe sa genereze oferta necesara, intr-un fisier separat numit output.txt.

![3](https://github.com/andreiserban1/ClientApp/assets/127241869/f04460a6-4755-40ff-a3fe-e22be8836325)

![4](https://github.com/andreiserban1/ClientApp/assets/127241869/3f28fb1c-a37a-491f-ae51-dc91ff064ec1)





  

  
