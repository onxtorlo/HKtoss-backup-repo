#!/bin/bash

# 색상 정의
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 배너 출력
echo -e "${BLUE}"
echo "╔══════════════════════════════════════════════╗"
echo "║                  PJA_Project                 ║"
echo "║          FastAPI + OpenAI Integration        ║"
echo "╚══════════════════════════════════════════════╝"
echo -e "${NC}"

# OpenAI API 키 확인 (환경변수에서)
if [ -z "$OPENAI_API_KEY" ]; then
    echo -e "${RED}❌ OPENAI_API_KEY 환경변수가 설정되지 않았습니다.${NC}"
    exit 1
fi

# API 키 유효성 간단 체크 (길이 확인)
if [ ${#OPENAI_API_KEY} -lt 20 ]; then
    echo -e "${RED}❌ 유효하지 않은 API 키입니다.${NC}"
    exit 1
fi

echo -e "${GREEN}✅ API 키가 설정되었습니다.${NC}"

# 서버 시작 정보 출력
echo -e "${BLUE}"
echo "🚀 FastAPI 서버를 시작합니다..."
echo "📡 포트: 8000"
echo "🌐 접속 주소: http://3.34.185.3:8000"
echo "📚 API 문서: http://3.34.185.3:8000/docs"
echo ""
echo "🔗 사용 가능한 엔드포인트:"
echo "  • POST /api/PJA/requirements/generate (요구사항 생성)"
echo "  • POST /api/PJA/json_text/generate (JSON 생성)"
echo "  • POST /api/PJA/json_ERD/generate (ERD 생성)"
echo "  • POST /api/PJA/recommend/generate (프로젝트 진행 추천)"
echo "  • POST /api/PJA/json_API/generate (API 생성)"
echo ""
echo -e "${YELLOW}서버를 중지하려면 Ctrl+C를 누르세요.${NC}"
echo -e "${NC}"

# FastAPI 서버 실행
exec uvicorn main:app --host 0.0.0.0 --port 8000

