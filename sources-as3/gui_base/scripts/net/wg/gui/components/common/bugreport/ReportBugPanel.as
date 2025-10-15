package net.wg.gui.components.common.bugreport
{
   import flash.events.TextEvent;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import flash.text.TextFormat;
   import flash.text.TextFormatAlign;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.events.UILoaderEvent;
   import net.wg.infrastructure.base.meta.IReportBugPanelMeta;
   import net.wg.infrastructure.base.meta.impl.ReportBugPanelMeta;
   
   public class ReportBugPanel extends ReportBugPanelMeta implements IReportBugPanelMeta
   {
      
      private static const REPORT_BUG_LINK_MARGIN:int = 2;
       
      
      public var reportBugLink:TextField;
      
      public var background:UILoaderAlt;
      
      private var isInited:Boolean = false;
      
      public function ReportBugPanel()
      {
         super();
         visible = false;
         tabEnabled = false;
         tabChildren = false;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.background.mouseChildren = false;
         this.background.mouseEnabled = false;
         var _loc1_:TextFormat = this.reportBugLink.defaultTextFormat;
         _loc1_.align = TextFormatAlign.CENTER;
         this.reportBugLink.defaultTextFormat = _loc1_;
         this.reportBugLink.setTextFormat(_loc1_);
         this.reportBugLink.y -= REPORT_BUG_LINK_MARGIN;
         this.reportBugLink.autoSize = TextFieldAutoSize.CENTER;
         App.utils.commons.addEmptyHitArea(this.background);
         App.utils.styleSheetManager.setLinkStyle(this.reportBugLink);
      }
      
      override protected function onDispose() : void
      {
         if(this.isInited)
         {
            this.background.removeEventListener(UILoaderEvent.COMPLETE,this.onBackgroundLoadComplieted);
            this.reportBugLink.removeEventListener(TextEvent.LINK,this.onReportBugLinkClick);
         }
         this.reportBugLink.styleSheet = null;
         this.reportBugLink = null;
         this.background.dispose();
         this.background = null;
         super.onDispose();
      }
      
      public function as_setHyperLink(param1:String) : void
      {
         if(!this.isInited)
         {
            this.background.addEventListener(UILoaderEvent.COMPLETE,this.onBackgroundLoadComplieted);
            this.background.source = RES_ICONS.MAPS_ICONS_LOBBY_REPORT_BUG_BACKGROUND;
            this.reportBugLink.addEventListener(TextEvent.LINK,this.onReportBugLinkClick);
            this.isInited = true;
         }
         this.reportBugLink.htmlText = param1;
      }
      
      private function onBackgroundLoadComplieted(param1:UILoaderEvent) : void
      {
         visible = true;
         this.background.removeEventListener(UILoaderEvent.COMPLETE,this.onBackgroundLoadComplieted);
      }
      
      private function onReportBugLinkClick(param1:TextEvent) : void
      {
         reportBugS();
      }
   }
}
