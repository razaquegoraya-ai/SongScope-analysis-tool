import time
from datetime import datetime

class ReportGenerator:
    def __init__(self):
        self.genre_bpm_ranges = {
            'EDM': (125, 130),
            'Hip-Hop': (85, 95),
            'Pop': (100, 120),
            'Rock': (110, 140),
            'Ballad': (60, 80)
        }

    def generate_report(self, song_name: str, composer: str, features: dict) -> dict:
        try:
            # Add metadata
            metadata = {
                "title": song_name,
                "composer": composer,
                "analysis_date": time.strftime("%B %d, %Y"),
                "version": "1.0"
            }

            # Calculate additional metrics
            energy_level = self._get_energy_level(features['energy'])
            suggested_genres = self._suggest_genres(features['tempo'], features['energy'])
            market_score = self._calculate_market_score(features)
            potential_score = self._calculate_potential_score(features)

            # Generate detailed report sections
            welcome = self._generate_welcome(song_name)
            overview = self._generate_overview(song_name, features)
            key_insights = self._generate_key_insights(song_name, features)
            technical_analysis = self._generate_technical_analysis(features)
            target_audience = self._generate_target_audience(song_name, features)
            market_potential = self._generate_market_potential(features)
            next_steps = self._generate_next_steps(features)
            improvement_suggestions = self._generate_improvement_suggestions(features)

            # Create structured report
            report = {
                "metadata": metadata,
                "welcome": welcome,
                "overview": overview,
                "key_insights": key_insights,
                "technical_analysis": technical_analysis,
                "target_audience": target_audience,
                "market_potential": market_potential,
                "next_steps": next_steps,
                "improvement_suggestions": improvement_suggestions,
                "numerical_metrics": {
                    "tempo": features['tempo'],
                    "energy": features['energy'],
                    "vocal_clarity": features.get('vocal_clarity', 0.75),
                    "instrumental_complexity": features.get('instrumental_complexity', 0.65),
                    "production_quality": features.get('production_quality', 0.8),
                    "engagement": features.get('engagement', 0.7)
                }
            }

            return report

        except Exception as e:
            print(f"Error generating report: {str(e)}")
            raise

    def _generate_welcome(self, song_name):
        return (f'Welcome to your detailed song analysis! Below, you\'ll find insights into how "{song_name}" sounds, '
                f'feels, and could shine even brighter. Whether you\'re a composer tweaking your work, a music supervisor '
                f'picking the perfect track, or a label eyeing its potential, we\'ve got you covered with clear, practical advice.')

    def _generate_overview(self, song_name, features):
        tempo_desc = "energetic" if features['tempo'] > 120 else "moderate" if features['tempo'] > 90 else "relaxed"
        energy_desc = "strong" if features['energy'] > 0.7 else "balanced" if features['energy'] > 0.4 else "subtle"
        vocal_clarity = features.get('vocal_clarity', 0.75)
        production_quality = features.get('production_quality', 0.8)

        return (f'"{song_name}" is a {tempo_desc} track with a tempo of {features["tempo"]:.1f} BPM, ' +
                f'giving it a {"danceable, upbeat" if features["tempo"] > 110 else "steady, flowing"} vibe. ' +
                f'It\'s got {energy_desc} energy ({features["energy"]:.2f}), ' +
                f'{"clear" if vocal_clarity > 0.7 else "balanced"} vocals ({vocal_clarity:.2f}), and ' +
                f'a {"polished" if production_quality > 0.75 else "solid"} production quality ({production_quality:.2f}). ' +
                f'Our analysis also picks up a "{features["mood"]}" mood, suggesting it\'s ' +
                f'{"a feel-good tune with pop appeal" if features["mood"].lower() in ["happy", "energetic"] else "perfect for creating atmosphere"}. ' +
                f'Here\'s how it breaks down—and how to make it even better!')

    def _generate_key_insights(self, song_name, features):
        insights = []

        # 1. Tempo & Rhythm
        tempo_insight = {
            "title": f"Tempo & Rhythm ({features['tempo']:.1f} BPM)",
            "meaning": f"This pace is {self._describe_tempo(features['tempo'])}—it's perfect for {self._get_tempo_use_case(features['tempo'])}.",
            "suggestion": self._get_tempo_suggestion(features['tempo'])
        }
        insights.append(tempo_insight)

        # 2. Energy
        energy_insight = {
            "title": f"Energy ({features['energy']:.2f}/1.0)",
            "meaning": f"Your song has {self._describe_energy(features['energy'])}, but there's room to play with dynamics.",
            "suggestion": self._get_energy_suggestion(features['energy'])
        }
        insights.append(energy_insight)

        # 3. Vocal Clarity
        vocal_clarity = features.get('vocal_clarity', 0.75)
        vocal_insight = {
            "title": f"Vocal Clarity ({vocal_clarity:.2f}/1.0)",
            "meaning": f"The vocals {self._describe_vocal_clarity(vocal_clarity)}.",
            "suggestion": self._get_vocal_suggestion(vocal_clarity)
        }
        insights.append(vocal_insight)

        # 4. Instrumental Complexity
        complexity = features.get('instrumental_complexity', 0.65)
        complexity_insight = {
            "title": f"Instrumental Complexity ({complexity:.2f}/1.0)",
            "meaning": f"The instruments {self._describe_complexity(complexity)}.",
            "suggestion": self._get_complexity_suggestion(complexity, song_name)
        }
        insights.append(complexity_insight)

        # 5. Mood & Genre
        mood_insight = {
            "title": f"Mood & Genre Fit ({features['mood']}, {self._suggest_primary_genre(features)})",
            "meaning": self._describe_mood_fit(features),
            "suggestion": self._get_mood_suggestion(features)
        }
        insights.append(mood_insight)

        # 6. Music Theory
        theory_insight = {
            "title": f"Music Theory (Key: {features['key']})",
            "meaning": f"Your song's in {features['key']}, {self._describe_key_character(features['key'])}.",
            "suggestion": self._get_theory_suggestion(features['key'])
        }
        insights.append(theory_insight)

        # 7. Mixing Quality
        mixing_insight = {
            "title": "Mixing Quality",
            "meaning": self._analyze_mix_quality(features),
            "suggestion": self._get_mixing_suggestion(features)
        }
        insights.append(mixing_insight)

        return insights

    def _describe_tempo(self, tempo):
        if tempo > 125:
            return "energetic and perfect for dance music"
        elif tempo > 110:
            return "upbeat and engaging"
        elif tempo > 90:
            return "steady and comfortable"
        else:
            return "relaxed and intimate"

    def _get_tempo_use_case(self, tempo):
        if tempo > 125:
            return "club tracks and high-energy content"
        elif tempo > 110:
            return "casual listening or upbeat scenes"
        elif tempo > 90:
            return "background music or relaxed content"
        else:
            return "intimate scenes or atmospheric moments"

    def _get_tempo_suggestion(self, tempo):
        if tempo > 125:
            return "Try adding breaks or slower sections (around 100 BPM) for dynamic contrast. This will give dancers a moment to catch their breath."
        elif tempo > 110:
            return "If you're aiming for a dancefloor hit, try speeding up to 128 BPM. That's a sweet spot for club tracks."
        elif tempo > 90:
            return "Experiment with double-time sections to add energy without changing the fundamental groove."
        else:
            return "Consider adding subtle percussion or a faster counter-melody to maintain interest while keeping the relaxed vibe."

    def _describe_energy(self, energy):
        if energy > 0.7:
            return "a powerful, driving feel that commands attention"
        elif energy > 0.4:
            return "a balanced, engaging energy level"
        else:
            return "a subtle, atmospheric quality"

    def _get_energy_suggestion(self, energy):
        if energy > 0.7:
            return "Add a quiet bridge or breakdown section—like a stripped-down verse with just vocals and a simple beat—before ramping back up. This contrast will make the loud parts hit harder."
        elif energy > 0.4:
            return "Try building to a more intense chorus by gradually adding layers of instruments and effects. This creates natural excitement."
        else:
            return "Experiment with adding subtle layers of percussion or pads to build tension without losing the intimate feel."

    def _describe_vocal_clarity(self, clarity):
        if clarity > 0.7:
            return "stand out nicely, making lyrics easy to hear—great for storytelling or catchy hooks"
        elif clarity > 0.4:
            return "blend well with the instruments, creating a balanced mix"
        else:
            return "sit back in the mix, creating an atmospheric effect"

    def _get_vocal_suggestion(self, clarity):
        if clarity > 0.7:
            return "Experiment with a touch of reverb (10-20%) on the vocals to add space without losing clarity. Also try subtle delay effects on specific phrases to create depth."
        elif clarity > 0.4:
            return "Use careful EQ around 2-4kHz to lift the vocals slightly without making them harsh. A gentle compressor can also help them cut through."
        else:
            return "If you want the vocals more upfront, try reducing reverb and bringing up the mid-range frequencies. For the current style, add textural vocal harmonies."

    def _describe_complexity(self, complexity):
        if complexity > 0.7:
            return "create a rich, detailed soundscape that rewards repeated listening"
        elif complexity > 0.4:
            return "blend well—not too empty, not too crowded—leaving space for everything to breathe"
        else:
            return "maintain a clean, minimalist arrangement that emphasizes key elements"

    def _get_complexity_suggestion(self, complexity, song_name):
        if complexity > 0.7:
            return f"Consider simplifying some sections to give listeners a break. You could strip back verses to core elements, saving the full complexity for chorus and bridge."
        elif complexity > 0.4:
            return f"Introduce a signature sound—like a unique synthesizer melody or distinctive bassline—to give '{song_name}' its own character."
        else:
            return "Try adding subtle counter-melodies or textural elements in specific sections to create more interest while maintaining clarity."

    def _suggest_primary_genre(self, features):
        if features['tempo'] > 125 and features['energy'] > 0.7:
            return "EDM-Leaning"
        elif features['tempo'] > 110 and features['energy'] > 0.6:
            return "Pop-Leaning"
        elif features['tempo'] < 90 and features['energy'] < 0.4:
            return "Ambient-Leaning"
        else:
            return "Pop-Leaning"

    def _describe_mood_fit(self, features):
        mood = features['mood'].lower()
        if mood in ['happy', 'energetic']:
            return "The song feels uplifting and positive, perfect for feel-good playlists or upbeat content"
        elif mood in ['relaxed', 'calm']:
            return "The track creates a peaceful atmosphere, ideal for relaxation or background music"
        else:
            return f"The {mood} mood gives the song a distinctive character that could work well in specific contexts"

    def _get_mood_suggestion(self, features):
        mood = features['mood'].lower()
        if mood in ['happy', 'energetic']:
            return "Add a catchy, singable hook in the chorus—something simple like a repeated phrase or melodic riff that listeners can easily remember."
        elif mood in ['relaxed', 'calm']:
            return "Try introducing subtle variations in texture and harmony to maintain interest while preserving the peaceful mood."
        else:
            return "Consider emphasizing the unique mood with complementary sound design or effects that enhance the emotional impact."

    def _describe_key_character(self, key):
        characters = {
            'C': 'which has a pure, open quality',
            'G': 'perfect for bright, optimistic feelings',
            'D': 'great for energetic, driving songs',
            'A': 'which can sound warm and engaging',
            'E': 'which often feels bright and assertive',
            'F': 'which has a warm, balanced character',
            'Bb': 'which can sound smooth and mellow'
        }
        return characters.get(key, 'which offers versatile possibilities')

    def _get_theory_suggestion(self, key):
        relative_keys = {
            'C': 'G or Am', 'G': 'D or Em', 'D': 'A or Bm',
            'A': 'E or F#m', 'E': 'B or C#m', 'F': 'C or Dm',
            'Bb': 'F or Gm'
        }
        return f"For an interesting twist, try modulating to {relative_keys.get(key, 'a related key')} in the bridge section. This can add emotional depth and keep listeners engaged."

    def _analyze_mix_quality(self, features):
        spectral_centroid = features.get('spectral_centroid', 2000)
        if spectral_centroid > 3000:
            return "The mix is bright, possibly with some high-frequency emphasis that could be smoothed out"
        elif spectral_centroid > 2000:
            return "The mix has good clarity and balance across frequencies"
        else:
            return "The mix has a warmer character that might benefit from some high-end enhancement"

    def _get_mixing_suggestion(self, features):
        spectral_centroid = features.get('spectral_centroid', 2000)
        if spectral_centroid > 3000:
            return "Use an equalizer to gently reduce frequencies above 10kHz by 1-2dB. This will maintain clarity while reducing any potential harshness."
        elif spectral_centroid > 2000:
            return "Try adding subtle saturation to the mid-range elements to enhance warmth without losing clarity."
        else:
            return "Consider a gentle high-shelf boost around 10kHz to add air and sparkle to the mix."

    def _generate_target_audience(self, song_name, features):
        sections = {
            "composers": self._get_composer_advice(song_name, features),
            "supervisors": self._get_supervisor_advice(features),
            "labels": self._get_label_advice(song_name, features)
        }
        return sections

    def _get_composer_advice(self, song_name, features):
        # Calculate key metrics
        engagement = features.get('engagement', 0.7)
        production_quality = features.get('production_quality', 0.8)
        vocal_clarity = features.get('vocal_clarity', 0.75)

        benefits = [
            "Creative & Technical Feedback: " +
            f"The report clearly shows that '{song_name}' already has a " +
            (f"strong rhythmic foundation and vocal delivery (clarity: {vocal_clarity:.2f}). " if vocal_clarity > 0.7
             else "developing foundation that can be enhanced. ") +
            "This data validates your compositional style and highlights areas for growth.",

            "Fine-tuning Arrangements: " +
            f"With {self._describe_complexity(features.get('instrumental_complexity', 0.65))}, you have a flexible canvas. " +
            "The report suggests that adding subtle dynamic variations or instrumental breaks could enhance the arrangement " +
            "without compromising its current clarity.",

            "Mixing Direction: " +
            f"Your vocals are effectively highlighted (clarity: {vocal_clarity:.2f}). " +
            (f"The noted {self._get_mixing_issues(features)} offers a specific target for your next mix revision, "
             "ensuring every sonic detail complements your creative vision.")
        ]

        specific_insights = [
            f"The clear rhythmic structure and {features['mood'].lower()} mood support your artistic intent. " +
            f"Your song's {features['key']} key signature ensures accessibility, making it an excellent candidate for " +
            "further experimentation with slight dynamic fluctuations—helping you maintain listener interest.",

            f"The {self._describe_tempo(features['tempo'])} tempo ({features['tempo']:.1f} BPM) and " +
            f"engagement score ({engagement:.2f}) indicate strong potential. Consider adding {self._get_arrangement_suggestion(features)} " +
            "to further enhance the emotional journey.",

            f"Production quality ({production_quality:.2f}) suggests " +
            (f"your mix is nearly broadcast-ready. Focus on {self._get_final_polish_suggestion(features)}"
             if production_quality > 0.75 else
             f"room for improvement. Prioritize {self._get_mix_improvement_priorities(features)}")
        ]

        return {
            "benefits": benefits,
            "specific_insights": specific_insights,
            "summary": self._generate_composer_summary(song_name, features)
        }

    def _get_supervisor_advice(self, features):
        # Calculate key metrics
        engagement = features.get('engagement', 0.7)
        production_quality = features.get('production_quality', 0.8)

        benefits = [
            "Quick Suitability Assessment: " +
            f"The detailed metrics (tempo: {features['tempo']:.1f} BPM, energy: {features['energy']:.2f}, " +
            f"mood: {features['mood'].lower()}) allow you to quickly determine if this track fits your project's specific " +
            "emotional and rhythmic requirements.",

            "Context Matching: " +
            f"The {self._describe_tempo(features['tempo'])} tempo and high engagement score ({engagement:.2f}) mean " +
            f"the track can effectively complement {self._get_context_suggestions(features)}. " +
            f"The {features['mood'].lower()} mood adds emotional authenticity.",

            "Technical Clarity Assurance: " +
            (f"While the report notes {self._get_mixing_issues(features)}, the overall production quality ({production_quality:.2f}) "
             "suggests broadcast-readiness with just minimal post-production tweaks." if production_quality > 0.75 else
             f"The production quality ({production_quality:.2f}) indicates some technical refinement may be needed before broadcast use.")
        ]

        specific_insights = [
            f"For your placements, this track's {self._describe_vocal_clarity(features.get('vocal_clarity', 0.75))} and " +
            f"{self._describe_complexity(features.get('instrumental_complexity', 0.65))} serve as strong assets.",

            f"The {features['mood'].lower()} mood and {self._describe_tempo(features['tempo'])} tempo align perfectly with " +
            f"{self._get_mood_use_cases(features)}. The {features['key']} key adds a {self._describe_key_character(features['key'])}.",

            f"Engagement metrics ({engagement:.2f}) assure you that audiences will respond positively, " +
            f"making it a compelling option for {self._get_specific_placement_suggestions(features)}."
        ]

        return {
            "benefits": benefits,
            "specific_insights": specific_insights,
            "summary": self._generate_supervisor_summary(features)
        }

    def _get_label_advice(self, song_name, features):
        # Calculate key metrics
        engagement = features.get('engagement', 0.7)
        production_quality = features.get('production_quality', 0.8)
        market_score = self._calculate_market_score(features)

        benefits = [
            "Market Readiness: " +
            f"The high reception scores (engagement: {engagement:.2f}, production: {production_quality:.2f}) signal that " +
            f"'{song_name}' has strong commercial potential. Market score: {market_score:.1f}/10 indicates " +
            ("immediate market viability." if market_score > 7 else "potential with strategic improvements."),

            "Quality Control & Investment: " +
            f"The detailed feedback on {self._get_key_quality_aspects(features)} provides a clear roadmap for " +
            f"optimization. {self._get_investment_recommendation(features)}",

            "Strategic Marketing: " +
            "The report's insights help in positioning the song within your catalog. The analysis provides concrete data " +
            "for making decisions on additional production investments to ensure maximum market impact."
        ]

        specific_insights = [
            f"Given the track's solid metrics (engagement: {engagement:.2f}, production: {production_quality:.2f}), " +
            (f"the song appears ready for wider distribution with only minor refinements needed." if production_quality > 0.75
             else f"focused improvements could significantly boost market potential."),

            f"The {features['mood'].lower()} mood and {self._describe_tempo(features['tempo'])} tempo make it an attractive " +
            f"candidate for {self._get_market_positioning(features)}. The {features['key']} key adds commercial appeal.",

            f"Strategic enhancements in {self._get_enhancement_priorities(features)} can optimize both the auditory experience " +
            "and market performance, boosting the track's competitive edge."
        ]

        return {
            "benefits": benefits,
            "specific_insights": specific_insights,
            "summary": self._generate_label_summary(song_name, features)
        }

    def _get_mixing_issues(self, features):
        if features.get('high_freq_noise', False):
            return "high-frequency noise"
        elif features.get('phase_issues', False):
            return "phase correlation issues"
        elif features.get('spectral_centroid', 2000) > 2500:
            return "bright-leaning frequency balance"
        else:
            return "minor mixing details"

    def _get_arrangement_suggestion(self, features):
        if features['energy'] > 0.7:
            return "dynamic contrasts through quieter bridge sections"
        elif features.get('instrumental_complexity', 0.65) < 0.6:
            return "subtle instrumental layers or counter-melodies"
        else:
            return "variations in texture between sections"

    def _get_final_polish_suggestion(self, features):
        if features.get('high_freq_noise', False):
            return "smoothing out high frequencies above 10kHz"
        elif features.get('phase_issues', False):
            return "checking mono compatibility"
        else:
            return "fine-tuning the overall frequency balance"

    def _get_mix_improvement_priorities(self, features):
        priorities = []
        if features.get('vocal_clarity', 0.75) < 0.7:
            priorities.append("vocal presence")
        if features.get('bass_presence', 0.7) < 0.7:
            priorities.append("low-end balance")
        if features.get('stereo_width', 0.7) < 0.6:
            priorities.append("stereo imaging")
        return " and ".join(priorities) if priorities else "overall mix balance"

    def _get_specific_placement_suggestions(self, features):
        if features['tempo'] > 120 and features['energy'] > 0.7:
            return "commercials, sports content, and high-energy media"
        elif features['tempo'] > 100:
            return "lifestyle content, brand messaging, and background scoring"
        else:
            return "emotional scenes, documentaries, and atmospheric content"

    def _get_key_quality_aspects(self, features):
        aspects = []
        if features.get('vocal_clarity', 0.75) > 0.7:
            aspects.append("vocal clarity")
        if features.get('production_quality', 0.8) > 0.75:
            aspects.append("production polish")
        if features.get('engagement', 0.7) > 0.7:
            aspects.append("listener engagement")
        return " and ".join(aspects) if aspects else "core elements"

    def _get_investment_recommendation(self, features):
        if features.get('production_quality', 0.8) > 0.85:
            return "Focus investment on marketing and promotion strategy."
        elif features.get('production_quality', 0.8) > 0.75:
            return "Consider minimal mixing refinements before full market push."
        else:
            return "Prioritize production improvements to maximize market potential."

    def _get_enhancement_priorities(self, features):
        priorities = []
        if features.get('high_freq_noise', False):
            priorities.append("frequency balance")
        if features.get('dynamic_range', 0.7) < 0.6:
            priorities.append("dynamic contrast")
        if features.get('stereo_width', 0.7) < 0.6:
            priorities.append("stereo imaging")
        return ", ".join(priorities) if priorities else "final polish"

    def _generate_composer_summary(self, song_name, features):
        return (f"Your track '{song_name}' shows {self._describe_potential(features)} potential. " +
                f"Focus on {self._get_primary_adjustment(features).lower()} to enhance its impact further.")

    def _generate_supervisor_summary(self, features):
        return (f"This track is best suited for {self._get_context_suggestions(features)}. " +
                f"Its {features['mood'].lower()} mood and {self._describe_tempo(features['tempo'])} tempo " +
                "make it versatile for various media applications.")

    def _generate_label_summary(self, song_name, features):
        market_score = self._calculate_market_score(features)
        return (f"With a market score of {market_score:.1f}/10, '{song_name}' " +
                ("is ready for market with minimal adjustments" if market_score > 7
                 else "shows promise with targeted improvements") + ". " +
                self._get_market_positioning(features))

    def _get_context_suggestions(self, features):
        if features['tempo'] > 120 and features['energy'] > 0.7:
            return "ideal for high-energy content, sports segments, or upbeat commercials"
        elif features['tempo'] > 100:
            return "suitable for lifestyle content, brand messaging, or background scoring"
        else:
            return "perfect for emotional scenes, documentary moments, or atmospheric content"

    def _get_mood_use_cases(self, features):
        mood = features['mood'].lower()
        if mood in ['happy', 'energetic']:
            return "positive brand messaging, lifestyle content, and uplifting scenes"
        elif mood in ['relaxed', 'calm']:
            return "reflective moments, nature scenes, and peaceful transitions"
        else:
            return f"specific emotional contexts that require a {mood} atmosphere"

    def _get_technical_readiness(self, features):
        production_quality = features.get('production_quality', 0.8)
        if production_quality > 0.85:
            return "Track is broadcast-ready with professional production quality"
        elif production_quality > 0.75:
            return "Minor technical adjustments recommended before broadcast use"
        else:
            return "Some production refinement needed for professional applications"

    def _get_market_positioning(self, features):
        if features['tempo'] > 120 and features['energy'] > 0.7:
            return "Strong potential in the dance/electronic and high-energy playlists"
        elif features['tempo'] > 100:
            return "Well-suited for mainstream pop and contemporary playlists"
        else:
            return "Ideal for mood-based and atmospheric playlists"

    def _get_distribution_strategy(self, features):
        engagement = features.get('engagement', 0.7)
        if engagement > 0.8:
            return "Priority for playlist pitching and active promotion"
        elif engagement > 0.6:
            return "Gradual rollout with focused genre-specific promotion"
        else:
            return "Consider niche market focus and targeted promotion"

    def _get_improvement_priority(self, features):
        production_quality = features.get('production_quality', 0.8)
        if production_quality > 0.85:
            return "Focus on marketing and promotion strategy"
        elif production_quality > 0.75:
            return "Minor mix refinements before full market push"
        else:
            return "Prioritize production improvements for market readiness"

    def _describe_potential(self, features):
        market_score = self._calculate_market_score(features)
        if market_score > 8:
            return "exceptional"
        elif market_score > 6:
            return "promising"
        else:
            return "developing"

    def _generate_market_potential(self, features):
        current_score = self._calculate_market_score(features)
        potential_score = self._calculate_potential_score(features)

        return {
            "current": {
                "score": current_score,
                "description": self._describe_current_potential(current_score)
            },
            "potential": {
                "score": potential_score,
                "description": self._describe_potential_score(potential_score, features)
            }
        }

    def _describe_current_potential(self, score):
        if score >= 8:
            return "Ready for release with strong commercial potential"
        elif score >= 6:
            return "Solid track with good potential for indie release or sync licensing"
        else:
            return "Has unique elements that could work well in specific markets"

    def _describe_potential_score(self, score, features):
        suggestions = []
        if features['tempo'] < 125 and features['energy'] > 0.6:
            suggestions.append("speed it up to 128 BPM")
        if features.get('vocal_clarity', 0.75) < 0.8:
            suggestions.append("enhance vocal clarity")
        if features.get('production_quality', 0.8) < 0.85:
            suggestions.append("polish the mix")

        if suggestions:
            return f"Could reach {score:.1f}/10 by: {', '.join(suggestions)}"
        return f"Already strong at {score:.1f}/10 - focus on marketing and promotion"

    def _generate_next_steps(self, features):
        steps = [
            "Open your music software and try these improvements:",
            self._get_primary_adjustment(features),
            self._get_secondary_adjustment(features),
            self._get_mixing_adjustment(features),
            "Upload the updated version to see how the scores improve!"
        ]
        return steps

    def _get_primary_adjustment(self, features):
        if features['tempo'] < 125 and features['energy'] > 0.6:
            return f"Adjust tempo to {self._get_optimal_tempo(features['tempo'])} BPM for better danceability"
        elif features['energy'] < 0.6:
            return "Add more dynamic contrast between sections"
        else:
            return "Fine-tune arrangement for maximum impact"

    def _get_secondary_adjustment(self, features):
        if features.get('vocal_clarity', 0.75) < 0.8:
            return "Enhance vocal presence with careful EQ and compression"
        elif features.get('instrumental_complexity', 0.65) < 0.7:
            return "Add subtle layers to enrich the arrangement"
        else:
            return "Refine existing elements for better blend"

    def _get_mixing_adjustment(self, features):
        if features.get('spectral_centroid', 2000) > 3000:
            return "Smooth out high frequencies above 10kHz"
        elif features.get('spectral_centroid', 2000) < 2000:
            return "Add gentle air and sparkle to the mix"
        else:
            return "Fine-tune overall frequency balance"

    def _get_optimal_tempo(self, current_tempo):
        if current_tempo < 100:
            return "100-110"
        elif current_tempo < 120:
            return "120-125"
        else:
            return "128-130"

    def _get_energy_level(self, energy):
        if energy > 0.7: return "High"
        elif energy > 0.4: return "Medium"
        else: return "Low"

    def _suggest_genres(self, tempo, energy):
        genres = []
        for genre, (min_bpm, max_bpm) in self.genre_bpm_ranges.items():
            if min_bpm <= tempo <= max_bpm:
                genres.append(genre)
        if energy > 0.7:
            genres.extend(['Dance', 'Electronic'])
        elif energy < 0.3:
            genres.extend(['Ambient', 'Chill'])
        return genres

    def _calculate_market_score(self, features):
        score = 6.0  # Base score
        if 115 <= features['tempo'] <= 130: score += 1
        if 0.5 <= features['energy'] <= 0.8: score += 1
        return min(score, 10.0)

    def _calculate_potential_score(self, features):
        return min(self._calculate_market_score(features) + 2.5, 10.0)

    def _generate_technical_analysis(self, features):
        return {
            "frequency_analysis": self._analyze_frequency_spectrum(features),
            "dynamics": self._analyze_dynamics(features),
            "stereo_field": self._analyze_stereo_field(features),
            "production_notes": self._generate_production_notes(features)
        }

    def _analyze_frequency_spectrum(self, features):
        spectral_centroid = features.get('spectral_centroid', 2000)
        spectral_rolloff = features.get('spectral_rolloff', 8000)

        return {
            "bass": self._analyze_bass_response(features),
            "mids": self._analyze_mids_response(features),
            "highs": self._analyze_highs_response(features),
            "overall_balance": "Well-balanced across the frequency spectrum" if 1800 < spectral_centroid < 2500 else
                             "Slightly bright-leaning" if spectral_centroid > 2500 else "Warm-leaning"
        }

    def _analyze_bass_response(self, features):
        return {
            "presence": features.get('bass_presence', 0.7),
            "clarity": features.get('bass_clarity', 0.65),
            "suggestion": "Consider adding subtle bass enhancement around 60-100Hz for more warmth" if features.get('bass_presence', 0.7) < 0.7 else
                        "Bass levels are well-balanced"
        }

    def _analyze_mids_response(self, features):
        return {
            "presence": features.get('mids_presence', 0.75),
            "clarity": features.get('mids_clarity', 0.7),
            "suggestion": "Try a gentle boost around 2-4kHz to enhance vocal presence" if features.get('mids_presence', 0.75) < 0.75 else
                        "Mid frequencies are well-represented"
        }

    def _analyze_highs_response(self, features):
        return {
            "presence": features.get('highs_presence', 0.8),
            "clarity": features.get('highs_clarity', 0.75),
            "noise_detected": features.get('high_freq_noise', False),
            "suggestion": "Use a de-esser or gentle high-shelf EQ cut above 10kHz" if features.get('high_freq_noise', False) else
                        "High frequencies are clean and clear"
        }

    def _analyze_dynamics(self, features):
        return {
            "dynamic_range": features.get('dynamic_range', 0.7),
            "peak_levels": features.get('peak_levels', -1.5),
            "average_loudness": features.get('average_loudness', -14),
            "suggestion": self._get_dynamics_suggestion(features)
        }

    def _get_dynamics_suggestion(self, features):
        if features.get('dynamic_range', 0.7) < 0.6:
            return "Consider adding more dynamic contrast between sections to enhance emotional impact"
        elif features.get('peak_levels', -1.5) > -1:
            return "Reduce peak levels slightly to prevent potential clipping"
        else:
            return "Dynamic range is appropriate for the style"

    def _analyze_stereo_field(self, features):
        return {
            "width": features.get('stereo_width', 0.7),
            "balance": features.get('stereo_balance', 0.5),
            "phase_issues": features.get('phase_issues', False),
            "suggestion": self._get_stereo_suggestion(features)
        }

    def _get_stereo_suggestion(self, features):
        if features.get('stereo_width', 0.7) < 0.6:
            return "Consider widening the stereo field for more immersive sound"
        elif features.get('phase_issues', False):
            return "Check for phase cancellation issues in the low frequencies"
        else:
            return "Stereo field is well-balanced"

    def _generate_production_notes(self, features):
        notes = []

        if features.get('high_freq_noise', False):
            notes.append("High-frequency noise detected - consider noise reduction")

        if features.get('phase_issues', False):
            notes.append("Phase correlation issues found - check mono compatibility")

        if features.get('clipping_detected', False):
            notes.append("Digital clipping detected - reduce levels or apply limiting")

        if not notes:
            notes.append("Overall production quality is good, with no major technical issues detected")

        return notes

    def _generate_improvement_suggestions(self, features):
        suggestions = []

        # Frequency balance suggestions
        if features.get('spectral_centroid', 2000) > 2500:
            suggestions.append({
                "category": "Frequency Balance",
                "issue": "Bright-leaning mix",
                "solution": "Use a gentle high-shelf EQ cut above 10kHz to reduce brightness",
                "benefit": "This will create a smoother, more professional sound"
            })

        # Dynamic range suggestions
        if features.get('dynamic_range', 0.7) < 0.6:
            suggestions.append({
                "category": "Dynamics",
                "issue": "Limited dynamic range",
                "solution": "Add quiet sections and build-ups between high-energy parts",
                "benefit": "This will create more emotional impact and keep listeners engaged"
            })

        # Stereo field suggestions
        if features.get('stereo_width', 0.7) < 0.6:
            suggestions.append({
                "category": "Stereo Image",
                "issue": "Narrow stereo field",
                "solution": "Use stereo widening techniques on specific elements (not bass)",
                "benefit": "This will create a more immersive listening experience"
            })

        return suggestions