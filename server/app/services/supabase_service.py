from ..extensions import supabase, init_extensions

def save_audio_analysis(user_id, analysis_result):
    init_extensions()  # Ensure extensions are initialized
    try:
        data = {
            'user_id': user_id,
            'category': analysis_result.get('category', ''),
            'sub_category': analysis_result.get('sub_category', ''),
            'summary': analysis_result.get('summary', ''),
            'key_issues': analysis_result.get('key_issues', []),
            'transcribed_text': analysis_result.get('transcribed_text', '')
        }
        
        response = supabase.table('audio_analysis').insert(data).execute()
        print(response)
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Error saving to Supabase: {str(e)}")
        raise
