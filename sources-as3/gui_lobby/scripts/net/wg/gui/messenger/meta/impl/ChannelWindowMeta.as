package net.wg.gui.messenger.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.infrastructure.base.AbstractWindowView;
   
   public class ChannelWindowMeta extends AbstractWindowView
   {
       
      
      public var showFAQWindow:Function;
      
      public function ChannelWindowMeta()
      {
         super();
      }
      
      public function showFAQWindowS() : void
      {
         App.utils.asserter.assertNotNull(this.showFAQWindow,"showFAQWindow" + Errors.CANT_NULL);
         this.showFAQWindow();
      }
   }
}
