# models/requests.py (기존 코드에 추가)
from pydantic import BaseModel, Field , validator
from typing import List, Optional, Any, Union, Dict


class Message(BaseModel):
    role: str = Field(..., description="메시지 작성자의 역할 (system, user, assistant)")
    content: str = Field(..., description="메시지 내용")

class RequirementsRequest(BaseModel):
    project_overview: str = Field(..., description="사용자의 아이디어 작성 내용")
    existing_requirements: str = Field(..., description="기존 요구사항 목록")
    additional_count: int = Field(5, ge=1, le=20, description="추가로 생성할 요구사항 개수")
    max_tokens: Optional[int] = Field(4000, ge=1, le=8000, description="생성할 최대 토큰 개수")
    temperature: float = Field(0.3, ge=0.0, le=2.0, description="생성 창의성 정도")
    model: str = Field("gpt-4o-mini", description="사용할 모델 이름")

class SummuryRequest(BaseModel):
    project_overview: str = Field(..., description="사용자의 아이디어 작성 내용")
    requirements : str = Field(..., description="추가 요구사항 목록")
    max_tokens: Optional[int] = Field(4000, ge=1, le=4000, description="생성할 최대 토큰 개수")
    temperature: float = Field(0.3, ge=0.0, le=2.0, description="생성 창의성 정도")
    model: str = Field("gpt-4o-mini", description="사용할 모델 이름")

# ERD 전체
class ERDRequest(BaseModel):
    project_overview: str = Field(..., description="사용자의 아이디어 작성 내용")
    requirements : str = Field(..., description="추가 요구사항 목록")
    project_summury : str = Field(..., description="프로젝트 요약 내용")
    max_tokens: Optional[int] = Field(4000, ge=1, le=8000, description="생성할 최대 토큰 개수")
    temperature: float = Field(0.3, ge=0.0, le=2.0, description="생성 창의성 정도")
    model: str = Field("gpt-4o", description="사용할 모델 이름")

# API 전체
class APIRequest(BaseModel):
    project_overview: str = Field(..., description="사용자의 아이디어 작성 내용")
    requirements : str = Field(..., description="추가 요구사항 목록")
    project_summury : str = Field(..., description="프로젝트 요약 내용")
    max_tokens: Optional[int] = Field(4000, ge=1, le=8000, description="생성할 최대 토큰 개수")
    temperature: float = Field(0.3, ge=0.0, le=2.0, description="생성 창의성 정도")
    model: str = Field("gpt-4o", description="사용할 모델 이름")

# 추천 내용
class RecommendationRequest(BaseModel):
    project_list: str = Field(..., description="팀 프로젝트에 작성된 리스트")
    max_tokens: Optional[int] = Field(3000, ge=1, le=3000, description="생성할 최대 토큰 개수")
    temperature: float = Field(0.3, ge=0.0, le=2.0, description="생성 창의성 정도")
    model: str = Field("gpt-4o-mini", description="사용할 모델 이름")

# 대시보드 파이프라인
class DashboardRequest(BaseModel) :
    user_log : str = Field(..., description="전처리 데이터")

# Category&Feature&Action 생성
class TaskGenerateRequest(BaseModel):
    project_summary: str = Field(..., description="프로젝트 개요 정보 (JSON 또는 Python 딕셔너리 형식)")

# 유사도 검색
class SearchshimilerRequest(BaseModel) :
    project_info : str = Field(..., description="유저의 project_info")
    top_k : int = 10
    recommendation_threshold : int = 0.2
