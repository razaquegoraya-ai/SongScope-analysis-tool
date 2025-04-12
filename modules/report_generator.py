import time

class ReportGenerator:
    def __init__(self):
        pass

    def generate_report(self, song_name: str, composer: str, features: dict) -> dict:
        try:
            # Determine energy level
            energy_level = "High" if features['energy'] > 0.6 else "Medium" if features['energy'] > 0.3 else "Low"
            
            # Generate interpretation
            interpretation = []
            if features['tempo'] > 140:
                interpretation.append("The fast tempo suggests an energetic and dynamic composition.")
            elif features['tempo'] > 100:
                interpretation.append("The moderate tempo indicates a balanced and engaging rhythm.")
            else:
                interpretation.append("The slower tempo creates a more contemplative and relaxed atmosphere.")
            
            interpretation.append(f"The composition in {features['key']} creates a distinct tonal character.")
            
            if features['energy'] > 0.6:
                interpretation.append("The high energy levels suggest an uplifting and powerful musical experience.")
            else:
                interpretation.append("The calmer energy profile indicates a more introspective and nuanced musical expression.")
            
            # Generate recommendations
            recommendations = []
            if features['tempo'] > 140:
                recommendations.append("Consider adding dynamic variations to maintain listener engagement.")
            elif features['tempo'] < 100:
                recommendations.append("Explore subtle rhythmic variations to enhance the musical flow.")
            
            if features['energy'] > 0.7:
                recommendations.append("Consider adding moments of contrast to create more musical tension and release.")
            elif features['energy'] < 0.3:
                recommendations.append("Explore opportunities to add subtle dynamic variations to maintain listener interest.")
            
            if features['spectral_centroid'] > 3000:
                recommendations.append("The bright spectral characteristics could be balanced with warmer tones.")
            elif features['spectral_centroid'] < 1500:
                recommendations.append("Consider adding some brighter elements to enhance the overall timbre.")
            
            # Create structured report
            report = {
                "tempo": features['tempo'],
                "key": features['key'],
                "energy": features['energy'],
                "mood": features['mood'],
                "spectral_centroid": features['spectral_centroid'],
                "spectral_rolloff": features['spectral_rolloff'],
                "interpretation": "\n".join(interpretation),
                "recommendations": "\n".join(recommendations)
            }
            
            return report
            
        except Exception as e:
            print(f"Error generating report: {str(e)}")
            raise