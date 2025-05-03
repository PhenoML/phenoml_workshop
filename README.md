# APIS vs. SDKs Workshop (by XPC and PhenoML)
This repo contains examples demonstrated during a workshop held on 05-02-2025. Check out the recording [here](https://www.youtube.com/watch?v=YGOZlYnGxvM)

## Getting access to Canvas Medical, Medplum, PhenoML, and Cerner 

### Canvas 
Get started with Canvas' Developer Sandbox [here](https://www.canvasmedical.com/emrs/developer-sandbox)!

### Medplum
Get started with [Medplum](https://www.medplum.com/docs)!

### Cerner
Check out Cerner's sandbox and documentation for Cerner FHIR APIs [here](https://docs.oracle.com/en/industries/health/millennium-platform-apis/mfrap/r4_overview.html)

### PhenoML 
- Check out developer docs and sign up for API access on the [PhenoML developer portal](https://developer.pheno.ml) to make FHIR API calls using language! 

## APIs

### Canvas
Create Patient in Canvas Medical via API

```
 cd api_examples/canvas
```
Now open `main.py` within the canvas folder in a new tab in replit and update the patient information for the patient you want to create

Go back to your shell tab and run the following command to create your patient!
```
 python3 main.py
```

### Cerner
Get Patient information from Cerner via API

Open a NEW shell tab and navigate to the Cerner folder by running these commands

```
 cd ..
```


```
 cd cerner
```

Go back to your shell tab and run the following command to search for a patient in the Cerner open sandbox!
```
 python3 main.py
```

### Medplum 
Create Condition in Medplum via API

Open a NEW shell tab and navigate to the Cerner folder by running these commands

```
 cd ..
```


```
 cd medplum
```

Go back to your shell tab and run the following command to create a condition for a patient in Medplum!
```
 python3 main.py
```

### PhenoML
Create Condition using :sparkles: language :sparkles: with lang2FHIR API and then post to Medplum and Canvas Medical. 
Search the 

Open a NEW shell tab and navigate to the PhenoML folder by running these commands
```
 cd ..
```


```
 cd phenoml
```

Go back to your shell tab and run the following command to create condition FHIR resources for Patients using language using lang2FHIR, then post to Medplum and Canvas Medical, and lastly run a search in Cerner using language. 
```
 python3 main.py
```

## SDKs

### Canvas Effect

Kerry will demo showing an updated patient chart layout by modifying the values in the layout effect.

### Medplum Lang2FHIR App

Check out github repo for [medplum provider lang2fhir app](https://github.com/PhenoML/medplum-provider-lang2fhir)
