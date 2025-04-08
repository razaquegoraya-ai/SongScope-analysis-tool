import time

class ReportGenerator:
    def generate_report(self, song_name, composer, features, reception_scores):
        report = f"""
Song Analysis Report for "{song_name}" by {composer}
Generated on {time.strftime('%B %d, %Y')}

1. Basic Information
-------------------
• Song: {song_name}
• Composer: {composer}
• Analysis Date: {time.strftime('%B %d, %Y')}

2. Musical Analysis
------------------
• Tempo: {features['tempo']:.1f} BPM
• Key: {features['theory']['key']}
• Mood: {features['mood']}
• Energy Level: {features['energy']:.2f}/1.0
• Vocal Clarity: {features['vocal_clarity']:.2f}/1.0
• Instrumental Complexity: {features['instrumental_complexity']:.2f}/1.0

3. Production Quality
--------------------
• Mixing Quality: {'Good' if not features['mixing']['high_freq_noise'] else 'Needs Improvement'}
• Production Score: {reception_scores['production_quality']:.2f}/1.0

4. Reception Analysis
--------------------
• Engagement Potential: {reception_scores['engagement']:.2f}/1.0
• Overall Quality Score: {reception_scores['production_quality']:.2f}/1.0

5. Recommendations
-----------------
{self._generate_recommendations(features, reception_scores)}
"""
        return report

    def _generate_recommendations(self, features, reception_scores):
        recommendations = []
        
        if features['vocal_clarity'] < 0.7:
            recommendations.append("• Consider improving vocal clarity through better mixing and EQ")
        
        if features['instrumental_complexity'] < 0.5:
            recommendations.append("• The instrumental arrangement could benefit from more complexity")
        
        if features['mixing']['high_freq_noise']:
            recommendations.append("• Address high-frequency noise issues in the mix")
        
        if reception_scores['engagement'] < 0.6:
            recommendations.append("• Work on increasing the song's energy and engagement")
        
        if not recommendations:
            recommendations.append("• Great job! The song is well-produced and engaging")
        
        return "\n".join(recommendations) 