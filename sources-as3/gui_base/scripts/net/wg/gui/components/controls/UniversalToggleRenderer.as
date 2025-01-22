package net.wg.gui.components.controls
{
   import net.wg.data.constants.UniversalBtnStylesConst;
   import net.wg.gui.components.controls.events.RendererEvent;
   import net.wg.gui.components.controls.universalBtn.UniversalBtn;
   import scaleform.clik.events.ButtonEvent;
   
   public class UniversalToggleRenderer extends ToggleRenderer
   {
       
      
      public function UniversalToggleRenderer()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         App.utils.universalBtnStyles.setStyle(UniversalBtn(btn),UniversalBtnStylesConst.STYLE_SLIM_BLACK);
         super.configUI();
      }
      
      override protected function enableButtonToggle() : void
      {
         UniversalBtn(btn).toggle = true;
      }
      
      override protected function updateButtonIcon() : void
      {
         UniversalBtn(btn).iconSource = _rendererData.value;
      }
      
      override protected function onBtnClickHandler(param1:ButtonEvent) : void
      {
         dispatchEvent(new RendererEvent(RendererEvent.ITEM_CLICK,_index,true));
      }
   }
}
