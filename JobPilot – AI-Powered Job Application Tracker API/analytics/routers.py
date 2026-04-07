from fastapi import APIRouter  , Depends , HTTPException
from sqlalchemy.orm import Session 
from Database.database import get_db
from jobs.model import JobApplication
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from analytics.schema import Summary ,Resume_detail , Resume_score

router = APIRouter(prefix='/analytics',tags =['Analytics'])


@router.get('/summary',response_model=Summary)
def get_summary(user_id:int,db:Session= Depends(get_db)):
    jobs = db.query(JobApplication).filter(JobApplication.user_id == user_id).all()
    if not jobs:
        raise HTTPException(status_code=404, detail = "User not avalible")

    summary_user = Summary(
        total_applied = len(jobs),
        interview = len([j for j in jobs if j.status =='interview']),
        offer = len([j for j in jobs if j.status =='offer']),
        rejected = len([j for j in jobs if j.status =='rejected']),
        pending = len([j for j in jobs if j.status =='pending'])
    )
    return summary_user

@router.post('/match-score',response_model=Resume_score)
def match_score(data:Resume_detail):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([data.resume , data.job_description])
    score = cosine_similarity(vectors[0],vectors[1])[0][0] *100
    
    if score >=70:  
        verdict = 'strong match'
    elif score >=40:
        verdict = "Average match"
    else:
        verdict = "Weak Match"
    
    

    return Resume_score(match_score = round(score,2),verdict=verdict)
