from part_1_core import step_1_structure, step_2_cloud_setup, step_3_docker_k8s
from part_2_infrastructure import step_4_database, step_5_agent, step_6_api_security
from part_3_intelligence import step_7_rbac, step_8_monitoring, step_9_ai_engine
from part_4_operations import step_10_alerts, step_11_compliance, step_12_testing
from part_5_business import step_13_docs, step_14_demo, step_15_business

if __name__ == "__main__":
    print("==================================================")
    print("      OMNITHREAD OS v6.0 - 15 ENTERPRISE STEPS    ")
    print("==================================================")
    
    step_1_structure()
    print("2. Cloud Setup:", step_2_cloud_setup())
    print("3. Docker/K8s:", step_3_docker_k8s())
    print("4. Database:", step_4_database())
    print("5. Agents:", step_5_agent())
    print("6. API Security:", step_6_api_security())
    print("7. RBAC Check (Admin, write):", step_7_rbac("Admin", "write"))
    print("8. Monitoring:", step_8_monitoring())
    print("9. AI Engine (CPU 90%):", step_9_ai_engine(90))
    step_10_alerts("Slack", "Critical server alert tested.")
    print("11. Compliance:", step_11_compliance())
    print("12. Testing:", step_12_testing())
    print("13. Docs:", step_13_docs())
    print("14. Demo:", step_14_demo())
    print("15. Business Ready:", step_15_business())
    print("==================================================")
    print("All 15 Enterprise Architecture Phases Loaded Successfully!")
