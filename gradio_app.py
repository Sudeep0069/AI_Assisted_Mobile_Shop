from mobile_shop import *
from display import *
from gemini_func import *
with gr.Blocks(title="AI Mobile Shop") as app:
    gr.Markdown(
        "# 📱 AI Mobile Shop\n"
        "### Python List + Dictionary + Gemini AI"
    )

    # Inventory
    with gr.Tab("📱 Inventory"):
        show_button = gr.Button("Show All Mobiles")
        inventory_output = gr.Markdown()

        show_button.click(
            show_inventory,
            outputs=inventory_output
        )

    # Search
    with gr.Tab("🔍 Search"):
        keyword = gr.Textbox(label="Brand / Model")
        search_button = gr.Button("Search")
        search_output = gr.Markdown()

        search_button.click(
            search_ui,
            inputs=keyword,
            outputs=search_output
        )

    # Budget
    with gr.Tab("💰 Budget"):
        budget = gr.Number(label="Maximum Budget")
        budget_button = gr.Button("Find Mobiles")
        budget_output = gr.Markdown()

        budget_button.click(
            budget_ui,
            inputs=budget,
            outputs=budget_output
        )

    # Add Mobile
    with gr.Tab("➕ Add Mobile"):
        brand = gr.Textbox(label="Brand")
        model = gr.Textbox(label="Model")
        price = gr.Number(label="Price")
        ram = gr.Textbox(label="RAM")
        storage = gr.Textbox(label="Storage")
        rating = gr.Number(label="Rating")
        stock = gr.Number(label="Stock")

        add_button = gr.Button("Add Mobile")
        add_output = gr.Textbox()

        add_button.click(
            add_ui,
            inputs=[
                brand, model, price, ram,
                storage, rating, stock
            ],
            outputs=add_output
        )

    # Delete
    with gr.Tab("🗑️ Delete"):
        mobile_id = gr.Number(label="Mobile ID")
        delete_button = gr.Button("Delete")
        delete_output = gr.Textbox()

        delete_button.click(
            delete_ui,
            inputs=mobile_id,
            outputs=delete_output
        )

    # Purchase
    with gr.Tab("🛒 Purchase"):
        purchase_id = gr.Number(label="Mobile ID")
        purchase_button = gr.Button("Purchase")
        purchase_output = gr.Textbox()

        purchase_button.click(
            purchase_ui,
            inputs=purchase_id,
            outputs=purchase_output
        )

    # Statistics
    with gr.Tab("📊 Statistics"):
        stats_button = gr.Button("Generate Statistics")
        stats_output = gr.Markdown()

        stats_button.click(
            statistics_ui,
            outputs=stats_output
        )

    # Gemini Assistant
    with gr.Tab("🤖 Gemini AI"):
        question = gr.Textbox(
            label="Ask Gemini",
            placeholder="Which phone is best under ₹60,000?",
            lines=4
        )

        ai_button = gr.Button("Ask Gemini")
        ai_output = gr.Markdown()

        ai_button.click(
            ask_gemini,
            inputs=question,
            outputs=ai_output
        )

    # Recommendation
    with gr.Tab("🎯 AI Recommendation"):
        ai_budget = gr.Number(label="Budget")

        ai_usage = gr.Textbox(
            label="Usage",
            placeholder="Gaming / Camera / Office / Study"
        )

        recommendation_button = gr.Button("Get Recommendation")
        recommendation_output = gr.Markdown()

        recommendation_button.click(
            ai_recommendation,
            inputs=[ai_budget, ai_usage],
            outputs=recommendation_output
        )

    # Comparison
    with gr.Tab("⚖️ AI Comparison"):
        phone1 = gr.Textbox(
            label="Phone 1",
            placeholder="Samsung Galaxy S25"
        )

        phone2 = gr.Textbox(
            label="Phone 2",
            placeholder="OnePlus OnePlus 13"
        )

        compare_button = gr.Button("Compare")
        compare_output = gr.Markdown()

        compare_button.click(
            compare_mobiles,
            inputs=[phone1, phone2],
            outputs=compare_output
        )
        
        app.launch(share=True)