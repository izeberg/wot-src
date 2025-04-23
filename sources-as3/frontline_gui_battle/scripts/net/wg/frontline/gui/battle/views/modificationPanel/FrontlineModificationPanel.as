package net.wg.frontline.gui.battle.views.modificationPanel
{
   import net.wg.data.constants.InvalidationType;
   import net.wg.frontline.gui.battle.views.modificationPanel.components.FrontlineModificationIcon;
   import net.wg.frontline.gui.battle.views.modificationPanel.components.FrontlineModificationInfo;
   import net.wg.frontline.gui.battle.views.modificationPanel.data.FrontlineModificationPanelVO;
   import net.wg.frontline.infrastructure.base.meta.IFrontlineModificationPanelMeta;
   import net.wg.frontline.infrastructure.base.meta.impl.FrontlineModificationPanelMeta;
   
   public class FrontlineModificationPanel extends FrontlineModificationPanelMeta implements IFrontlineModificationPanelMeta
   {
      
      private static const FRAME_SHOW:String = "show";
      
      private static const FRAME_HIDE:String = "hide";
       
      
      public var _data:FrontlineModificationPanelVO = null;
      
      public var iconMC:FrontlineModificationIcon = null;
      
      public var titleTxt:FrontlineModificationInfo = null;
      
      public var descriptionTxt:FrontlineModificationInfo = null;
      
      public function FrontlineModificationPanel()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._data)
         {
            this._data = null;
         }
         this.iconMC.dispose();
         this.iconMC = null;
         this.titleTxt.dispose();
         this.titleTxt = null;
         this.descriptionTxt.dispose();
         this.descriptionTxt = null;
         super.onDispose();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.mouseEnabled = this.mouseChildren = false;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._data && isInvalid(InvalidationType.DATA))
         {
            this.iconMC.setIcon(this._data.modificationIconPath);
            this.titleTxt.setLabel(this._data.modificationTitle);
            this.descriptionTxt.setLabel(this._data.modificationDescription);
         }
      }
      
      override protected function setData(param1:FrontlineModificationPanelVO) : void
      {
         this._data = param1;
         invalidateData();
      }
      
      public function as_setVisible(param1:Boolean) : void
      {
         this.gotoAndPlay(!!param1 ? FRAME_SHOW : FRAME_HIDE);
      }
   }
}
