#!/bin/bash

# Quick Test Script for StudyHub
# Tests all major components in 30 seconds

set -e

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}"
echo "╔═══════════════════════════════════════════════════════╗"
echo "║                                                       ║"
echo "║         🧪 StudyHub Quick Test Suite 🧪              ║"
echo "║                                                       ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Counters
total=0
passed=0
failed=0

# Test function
run_test() {
    local test_name=$1
    local test_command=$2
    
    ((total++))
    echo -n "[$total] Testing $test_name... "
    
    if eval "$test_command" > /dev/null 2>&1; then
        echo -e "${GREEN}✓ PASSED${NC}"
        ((passed++))
        return 0
    else
        echo -e "${RED}✗ FAILED${NC}"
        ((failed++))
        return 1
    fi
}

# Start tests
echo -e "\n${YELLOW}🔍 Phase 1: Docker Services${NC}"
run_test "Docker Compose" "docker-compose --version"
run_test "Backend Container" "docker-compose ps backend | grep -q Up"
run_test "Frontend Container" "docker-compose ps frontend | grep -q Up"
run_test "Database Container" "docker-compose ps db | grep -q healthy"
run_test "Redis Container" "docker-compose ps redis | grep -q Up"

echo -e "\n${YELLOW}🌐 Phase 2: Network Connectivity${NC}"
run_test "Backend Health" "curl -sf http://localhost:8000/api/grades/"
run_test "Frontend Health" "curl -sf http://localhost/"
run_test "Admin Panel" "curl -sf http://localhost:8000/admin/"

echo -e "\n${YELLOW}📊 Phase 3: API Endpoints${NC}"
run_test "Grades API" "curl -sf http://localhost:8000/api/grades/ | grep -q 'level'"
run_test "Subjects API" "curl -sf http://localhost:8000/api/subjects/"
run_test "Chapters API" "curl -sf http://localhost:8000/api/chapters/"
run_test "Materials API" "curl -sf http://localhost:8000/api/materials/"
run_test "Quizzes API" "curl -sf http://localhost:8000/api/quizzes/"
run_test "Flashcards API" "curl -sf http://localhost:8000/api/flashcards/"

echo -e "\n${YELLOW}🗄️ Phase 4: Database${NC}"
run_test "Database Connection" "docker-compose exec -T backend python manage.py check --database default"
run_test "Migrations Status" "docker-compose exec -T backend python manage.py showmigrations | grep -q '\[X\]'"

echo -e "\n${YELLOW}📦 Phase 5: Data Verification${NC}"
run_test "Grades Data Exists" "curl -sf http://localhost:8000/api/grades/ | grep -q '\"count\":[1-9]'"
run_test "Subjects Data" "curl -sf http://localhost:8000/api/subjects/"

echo -e "\n${YELLOW}🔍 Phase 6: Logs Check${NC}"
run_test "Backend Logs Clean" "! docker-compose logs backend | grep -i 'error.*critical'"
run_test "Database Logs Clean" "! docker-compose logs db | grep -i 'fatal'"

# Results
echo -e "\n${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                  TEST SUMMARY                         ║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
echo ""
echo "  Total Tests:  $total"
echo -e "  ${GREEN}Passed:       $passed${NC}"
echo -e "  ${RED}Failed:       $failed${NC}"
echo ""

# Calculate percentage
percentage=$((passed * 100 / total))

if [ $failed -eq 0 ]; then
    echo -e "${GREEN}╔═══════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║         ✅ ALL TESTS PASSED! (100%)                   ║${NC}"
    echo -e "${GREEN}║     Your StudyHub installation is working! 🎉        ║${NC}"
    echo -e "${GREEN}╚═══════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo "🌐 Access your application:"
    echo "   Frontend:  http://localhost"
    echo "   Backend:   http://localhost:8000/api/"
    echo "   Admin:     http://localhost:8000/admin/"
    echo ""
    exit 0
elif [ $percentage -ge 80 ]; then
    echo -e "${YELLOW}╔═══════════════════════════════════════════════════════╗${NC}"
    echo -e "${YELLOW}║      ⚠️  MOSTLY WORKING ($percentage%)                    ║${NC}"
    echo -e "${YELLOW}║   Some non-critical tests failed                      ║${NC}"
    echo -e "${YELLOW}╚═══════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo "Check logs for details: docker-compose logs"
    exit 1
else
    echo -e "${RED}╔═══════════════════════════════════════════════════════╗${NC}"
    echo -e "${RED}║          ❌ TESTS FAILED ($percentage%)                      ║${NC}"
    echo -e "${RED}║     Several critical issues detected                  ║${NC}"
    echo -e "${RED}╚═══════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo "🔧 Troubleshooting:"
    echo "   1. Check logs: docker-compose logs -f"
    echo "   2. Restart services: docker-compose restart"
    echo "   3. Check .env configuration"
    echo "   4. Read TESTING_GUIDE.md for detailed help"
    echo ""
    exit 1
fi
