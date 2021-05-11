
#ifndef YOURPRIMARYGENERATORACTION_HH
#define YOURPRIMARYGENERATORACTION_HH

#include "G4VUserPrimaryGeneratorAction.hh"
#include "globals.hh"

class YourDetectorConstruction;
class G4ParticleGun;
class G4Event;
class G4String;

class YourPrimaryGeneratorAction : public G4VUserPrimaryGeneratorAction {
	public:
		YourPrimaryGeneratorAction(YourDetectorConstruction* det);
		virtual ~YourPrimaryGeneratorAction();
		
		virtual void GeneratePrimaries(G4Event* anEvent);
		
		void SetDefaultKinematic();
		void UpdatePosition();
		const G4String& GetParticleName() const;
		G4double GetParticleEnergy() const;
		
	private:
		YourDetectorConstruction* fYourDetector;
		G4ParticleGun* fParticleGun;
	};
	
#endif
